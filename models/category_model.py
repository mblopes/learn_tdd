from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from .base_model import BaseModel


class Category(BaseModel):
    __tablename__ = "CATEGORY"
    name = Column(String(length = 50), nullable=False)
    description = Column(String(length = 150), nullable=True)
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not name.strip():
            raise ValueError('Name can not be empty')
        if len(name) > 50:
            raise ValueError('Name is bigger than 50 characters')
        return name

    @validates('description')
    def validate_name(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description must be a string')
        if len(description) > 150:
            raise ValueError('Description is bigger than 150 characters')
        return description
