from models.category_model import Category
from models.base_model import BaseModel
import pytest


class TestCategoryModel:
    @pytest.fixture
    def category_instance(self):
        category = Category('category name', 'description')
        return category

    @pytest.mark.parametrize("name, description", [
        ('test name', 'test description'),
        ('t', ''),
        ('t'*100, 't'*150)
    ])
    def test_category_instance(self, category_instance, name, description):
        category_instance.name = name
        category_instance.description = description
        assert isinstance(category_instance, Category)
        assert isinstance(category_instance, BaseModel)

    def test_category_args(self, category_instance):
        category_instance.name = 'test name'
        category_instance.description = 'test description'
        assert category_instance.name is 'test name'
        assert category_instance.description is 'test description'

    @pytest.mark.parametrize("name", [
        None, 5, 5.0, [1, 2, 3],
        ('a', 'b', 'c'),
        Category('name', 'description'),
        {'name': 'test name',
         'description': 'test description'}
    ])
    def test_name_not_instance_str(self, category_instance, name):
        with pytest.raises(TypeError):
            category_instance.name = name

    def test_name_blank_spaces(self, category_instance):
        with pytest.raises(ValueError):
            category_instance.name = ''

    @pytest.mark.parametrize("description", [
        None, 5, 5.0, [1, 2, 3],
        ('a', 'b', 'c'),
        Category('name', 'description'),
        {'name': 'test name',
         'description': 'test description'}
    ])
    def test_description_not_instance_str(self, category_instance, description):
        with pytest.raises(TypeError):
            category_instance.description = description

    def test_name_too_big(self, category_instance):
        with pytest.raises(ValueError):
            category_instance.name = 'test name'*100

    def test_description_not_none(self, category_instance):
        with pytest.raises(TypeError):
            category_instance.description = None

    def test_description_too_big(self, category_instance):
        with pytest.raises(ValueError):
            category_instance.description = 'test description'*150
