import sys
sys.path.append('.')

from models.category_model import Category
from models.base_model import BaseModel
import pytest

class TestCategoryModel:

    @pytest.mark.parametrize("name, description", [
        ('N',''), 
        ('N'*100, 'D'*150), 
        ('N' * 50,'D' * 120),
        ('N' * 45,'D' * 120)
    ])
    def test_category_instance(self, name, description):
        category = Category(name, description)
        assert isinstance(category, Category)
        assert isinstance(category, BaseModel)

    def test_name_not_instance_str(self):
        with pytest.raises(TypeError):
            Category(None, 'test description')

    def test_name_min_len(self):
        name = 'N'
        description = ''
        category = Category(name, description)
        assert category.name is name        

    @pytest.mark.parametrize("name, description", [
        (10, 'test description'),
        (10.5, 'test description'),
        (False, 'test description')
    ])
    def test_name_blank_spaces(self, name, description):
        with pytest.raises(ValueError):
            category = Category('', 'test description')

    def test_name_too_big(self):
        with pytest.raises(ValueError):
            category = Category('test name'*100, 'test description')

    def test_description_not_none(self):
        with pytest.raises(TypeError):
            category = Category('test name', None)

    def test_description_too_big(self):
        with pytest.raises(ValueError):
            category = Category('test name', 'test description'*200)
