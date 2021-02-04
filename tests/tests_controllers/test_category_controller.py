from controllers.base_controller import BaseController
from controllers.category_controller import CategoryController
from models.category_model import Category
import pytest


class TestCategoryController:
    @pytest.fixture
    def category_instance(self):
        category = Category('category name', 'description')
        return category

    @pytest.fixture
    def category_controller(self):
        controller = CategoryController()
        return controller

    def test_category_controller_instance(self, category_controller):
        assert isinstance(category_controller, BaseController)
        assert isinstance(category_controller, CategoryController)

    def test_read_all_should_return_list(self, category_controller):
        result = category_controller.read_all()
        assert isinstance(result, list)
        assert all(isinstance(item, Category) for item in result)

    def test_create_method(self, category_instance, category_controller):
        result = category_controller.create(category_instance)
        assert result.id is not None
        assert result.name == category_instance.name
        assert result.description == category_instance.description
        category_controller.delete(result)

    def test_update_method(self, category_instance, category_controller):
        created = category_controller.create(category_instance)
        created.name = 'Team 2'
        created.description = 'Test 2'
        result = category_controller.update(created)
        assert result.id is not None
        assert result.name is created.name
        assert result.description is created.description

        category_controller.delete(result)

    def test_delete_method(self, category_controller, category_instance):
        created = category_controller.create(category_instance)
        category_controller.delete(created)
        with pytest.raises(Exception) as exc:
            category_controller.read_by_id(created.id)
            assert str(exc.value) == 'Object not found in the database.'

    def test_read_by_id_should_return_team(self, category_controller, category_instance):
        created = category_controller.create(category_instance)
        result = category_controller.read_by_id(created.id)

        assert isinstance(result, Category)
        assert result.name == created.name
        assert result.description == created.description
        category_controller.delete(created)

    def test_read_by_id_with_invalid_id_should_raise_exception(
            self, category_controller, category_instance
    ):
        with pytest.raises(Exception) as exc:
            category_controller.read_by_id(71289379)
            assert str(exc.value) == 'Object not found in the database.'
