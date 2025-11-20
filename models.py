"""
User Management API - Data Models

This module defines Pydantic models for data validation and serialization.
"""

from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User data model representing a user in the system.
    
    Attributes:
        id: Unique identifier for the user
        name: Full name of the user
        phone_no: Phone number of the user
        address: Physical address of the user
    """
    id: int = Field(..., description="Unique identifier for the user", gt=0)
    name: str = Field(..., description="Full name of the user", min_length=1)
    phone_no: str = Field(..., description="Phone number of the user", min_length=1)
    address: str = Field(..., description="Physical address of the user", min_length=1)
    
    class Config:
        """Pydantic configuration"""
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "phone_no": "+1234567890",
                "address": "123 Main St, City, Country"
            }
        }
