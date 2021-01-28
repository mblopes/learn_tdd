import sys
sys.path.append('.')

from models.category_model import Category
from models.base_model import BaseModel


class TestCategoryModel:
    def test_name_none(self):
        try:
            category = Category(None, 'Category test')
            raise NotImplementedError('Not implemented exception')
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_name_blank(self):
        try:
            category = Category(' ', 'Category test')
            raise NotImplementedError('Not implemented exception')
        except Exception as error:
            assert isinstance(error, ValueError)
        
