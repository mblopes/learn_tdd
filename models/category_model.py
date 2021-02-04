from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from models.base_model import BaseModel
from utils.validators import validate_not_empty, validate_type, validate_len


class Category(BaseModel):
    __tablename__ = "CATEGORY"

    name = Column(String(length=100), nullable=False)
    description = Column(String(length=150), nullable=True)
    
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name: str) -> str:
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        return validate_len(name, 100, key)

    @validates('description')
    def validate_description(self, key, description: str) -> str:
        description = validate_type(description, str, key)
        return validate_len(description, 150, key)
