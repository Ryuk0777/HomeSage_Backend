from pydantic import BaseModel, Field, field_validator
from typing import Literal
import pandas as pd
import json

COLUMNS_NAME = ["Zip Code", "Beds", "Baths", "Living Space", "Zip Code Population", "Zip Code Density", 
                "Median Household Income"]

with open("data/america/zip_codes.json" ,'r', encoding='utf-8') as file:
    ZIP_CODES = json.load(file)


class XValues(BaseModel):
    Zip_Code: int 
    Beds: int = Field(..., ge=0, description="No of beds") 
    Baths: int = Field(..., ge=0, description="No of baths")
    Living_Space: float = Field(..., ge=0, description="Value of Living_Space should be non negative")
    Zip_Code_Population: float = Field(..., ge=0, description="Value of Zip Code Population should be non negative")
    Zip_Code_Density: float = Field(..., ge=0, description="Value of Zip Code Density should be non negative")
    Median_Household_Income: float = Field(..., ge=0, description="Value of Average House Income should be non negative")



    @field_validator('Zip_Code', mode='before')
    @classmethod
    def validate_zip_code(cls, value):
        if value not in ZIP_CODES:
            raise ValueError(f'Zip_Code {value} is not not a valid ZIP codes.')
        return value


    def get(self):

        data = [
            self.Zip_Code,
            self.Beds,
            self.Baths,
            self.Living_Space,
            self.Zip_Code_Population,
            self.Zip_Code_Density,
            self.Median_Household_Income
        ]

        return pd.DataFrame([data], columns=COLUMNS_NAME)