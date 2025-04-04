from pydantic import BaseModel, Field, field_validator
from typing import Literal
import pandas as pd
import json


COLUMNS_NAME = ['Rooms', 'Bathrooms', 'Car Parks', 'Size in sq.ft',
       'Land', 'Landed',
       'Townhouse', 'Partly Furnished',
       'Unfurnished', 'Price_per_sqft']



with open("data/malaysia/Malaysia_property_mapping.json") as f:
    PROPERTY_MAPPING_1 = json.load(f)



PROPERTY_MAPPING_2 = {
    "High-Rise": [0, 0, 0],
    "Land": [1, 0, 0],
    "Landed Property": [0, 1, 0],
    "Townhouse": [0, 0, 1],
    }

FURNISHING_MAPPING = {
    "Fully Furnished": [0, 0],
    "Partly Furnished": [1, 0], 
    "Unfurnished": [0, 1],
}


def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
        
    return flattened



class XValues(BaseModel):
    rooms: int = Field(..., ge=0, description="Room number should not be negative")
    bathrooms: int = Field(..., ge=0, description="Bathrooms number should not be negative")
    car_Parks: int = Field(..., ge=0, description="Car parking number should not be negative")
    size_in_sq_ft: float = Field(..., ge=0, description="size in sq.ft should be positive")

    property_type: Literal["Condominium", "Apartment", "Flat", "Serviced Residence",
                           "Bungalow", "Semi-detached House", "Terrace House",
                           "Cluster House", "Townhouse", "Residential Land", "Bungalow Land"] 
    
    furnishing: Literal["Fully Furnished", "Partly Furnished", "Unfurnished"]

    price_per_sqft: float = Field(..., ge=0, description="Price per sq.ft should be positive")


    @field_validator('property_type', mode='after')
    @classmethod
    def validate_property_type(cls, value):
        value = PROPERTY_MAPPING_1[value]
        value = PROPERTY_MAPPING_2[value]
        return value
    
    @field_validator('furnishing', mode='after')
    @classmethod
    def validate_furnishing(cls, value):
        value = FURNISHING_MAPPING[value]
        return value
    

    def get(self):
        data = [
            self.rooms,
            self.bathrooms,
            self.car_Parks,
            self.size_in_sq_ft,
            *self.property_type,
            *self.furnishing,
            self.price_per_sqft
        ]

        return pd.DataFrame([data], columns=COLUMNS_NAME)
