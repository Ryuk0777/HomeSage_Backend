from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated, List
import json
import pandas as pd

with open("data\india\loaction.json" ,'r', encoding='utf-8') as file:
    STATE_CITY_MAPPING = json.load(file)



ORDINAL_MAPPING = {
    "Unfurnished":0, "Semi-furnished":1, "Furnished":2,
    "Low":0, "Medium":1, "High":2,
    "No":0, "Yes":1,
    "Under-Construction":0, "Ready-to-Move":1,
}

ONE_HOT_MAPPING = {
    "Apartment": [0,0], "Independent-House":[1,0], "Villa": [0, 1],
    "Builder":[1,0], "Owner":[0,1], "Broker":[0,0]
}

AMENITIES_LIST = ["Clubhouse", "Garden", "Gym", "Playground", "Pool"]



COLUMNS_NAMES = [
    'BHK', 'Size_in_SqFt', 'Price_per_SqFt', 'Furnished_Status', 'Floor_No',
    'Total_Floors', 'Age_of_Property', 'Nearby_Schools', 'Nearby_Hospitals',
    'Public_Transport_Accessibility', 'Parking_Space', 'Security',
    'Availability_Status', 'Latitude', 'Longitude', 'House', 'Villa',
    'Owner_Type_Builder', 'Owner_Type_Owner', 'Clubhouse', 'Garden', 'Gym',
    'Playground', 'Pool'
    ]


class XValues(BaseModel):
    BHK: int
    Size_in_SqFt: float
    Price_per_SqFt: float
    Furnished_Status: Literal["Unfurnished", "Semi-furnished", "Furnished"]
    Floor_No: int
    Total_Floors: int
    Age_of_Property: float
    Nearby_Schools: int
    Nearby_Hospitals: int
    Public_Transport_Accessibility: Literal["Low", "Medium", "High"]
    Parking_Space: Literal["No", "Yes"]
    Security: Literal["No", "Yes"]
    
    Availability_Status: Literal["Under-Construction", "Ready-to-Move"]

    state: Literal["Tamil Nadu", "Maharashtra", "Punjab", "Rajasthan", "West Bengal", 
                   "Chhattisgarh", "Delhi", "Jharkhand", "Telangana", "Karnataka", 
                   "Uttar Pradesh", "Assam", "Uttarakhand", "Bihar", "Gujarat", "Haryana", 
                   "Andhra Pradesh", "Madhya Pradesh", "Kerala", "Odisha"]
    
    city: Literal["Chennai", "Coimbatore", "Pune", "Nagpur", "Mumbai", "Ludhiana",
                   "Amritsar", "Jodhpur", "Jaipur", "Durgapur", "Kolkata", "Bilaspur",
                   "Raipur", "New Delhi", "Dwarka", "Ranchi", "Jamshedpur", "Warangal", 
                   "Hyderabad", "Bangalore", "Mysore", "Mangalore", "Lucknow", "Noida",
                   "Silchar", "Guwahati", "Dehradun", "Haridwar", "Gaya", "Patna", "Ahmedabad",
                   "Surat", "Faridabad", "Gurgaon", "Visakhapatnam", "Vijayawada", "Bhopal", 
                   "Indore", "Trivandrum", "Kochi", "Cuttack", "Bhubaneswar"]

    property_Type: Literal["Apartment", "Independent-House", "Villa"]
    owner_Type: Literal["Builder", "Owner", "Broker"]
    Amenities: Annotated[
        List[Literal["Clubhouse", "Garden", "Gym", "Playground", "Pool"]],
        Field(min_length=1, max_length=5)
    ]


    @field_validator("Amenities", mode='before')
    @classmethod
    def handle_amenities(cls, values):
        if isinstance(values, list):
            return list(dict.fromkeys(values))
        return values


    @field_validator("Furnished_Status", "Public_Transport_Accessibility", 
                     "Parking_Space", "Security", "Availability_Status", mode="after")
    @classmethod
    def handle_ordinal_field(cls, field):
        return ORDINAL_MAPPING[field]
    

    @field_validator("city", mode="after")
    @classmethod
    def handle_state_city(cls, value, field_name):
        try:
            return STATE_CITY_MAPPING[field_name.data['state'].lower().capitalize()][value.lower().capitalize()]
        except KeyError:
            print('Error in handle state city')
            return None 


    @field_validator("property_Type", "owner_Type", mode="after")
    @classmethod
    def handle_one_hot_field(cls, field):
        return ONE_HOT_MAPPING[field]


    @field_validator("Amenities", mode='after')
    @classmethod
    def handle_amenities_list(cls, field):
        return [1 if amenity in field else 0 for amenity in AMENITIES_LIST]


    def location_status(self) -> bool:
        if self.city == None:
            return False
        else:
            return True
        

    def get(self):
        data =[
        self.BHK, self.Size_in_SqFt, self.Price_per_SqFt, self.Furnished_Status, self.Floor_No, self.Total_Floors,
        self.Age_of_Property, self.Nearby_Schools, self.Nearby_Hospitals, self.Public_Transport_Accessibility, 
        self.Parking_Space, self.Security, self.Availability_Status, *self.city, *self.property_Type, *self.owner_Type, 
        *self.Amenities
        ]

        return pd.DataFrame([data], columns=COLUMNS_NAMES)