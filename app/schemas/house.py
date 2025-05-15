from pydantic import BaseModel, Field
from typing import Optional

class HouseFeatures(BaseModel):
    """Schema for house features input"""
    sqft_living: float = Field(..., description="Square footage of living space", ge=290, le=5420)
    grade: float = Field(..., description="Overall grade given to the housing unit", ge=1, le=13)
    bathrooms: float = Field(..., description="Number of bathrooms", ge=0, le=8)
    bedrooms: float = Field(..., description="Number of bedrooms", ge=0, le=11)
    waterfront: int = Field(..., description="Whether the house has a waterfront view (0 or 1)", ge=0, le=1)
    view: int = Field(..., description="Quality of view (0-4)", ge=0, le=4)
    sqft_basement: float = Field(..., description="Square footage of basement", ge=0, le=2720)
    yr_built: int = Field(..., description="Year when house was built", ge=1900, le=2015)
    lat: float = Field(..., description="Latitude coordinate", ge=47.1559, le=47.7776)
    long: float = Field(..., description="Longitude coordinate", ge=-122.519, le=-121.315)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "sqft_living": 2000,
                "grade": 8,
                "bathrooms": 2.5,
                "bedrooms": 3,
                "waterfront": 0,
                "view": 0,
                "sqft_basement": 0,
                "yr_built": 1990,
                "lat": 47.6062,
                "long": -122.3321
            }
        }
    }

class PredictionResponse(BaseModel):
    """Schema for prediction response"""
    predicted_price: float
    features: HouseFeatures