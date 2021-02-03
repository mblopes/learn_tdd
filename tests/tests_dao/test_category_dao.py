from sqlalchemy.orm.exc import UnmappedInstanceError
from dao.category_dao import CategoryDao
from models.category_model import Category
from dao.base_dao import BaseDao
import pytest


class TestCategoryDao:
    @pytest.fixture
    def category_instance(self):
        category = Category('category name', 'description')
        return category

    @pytest.fixture
    def category_dao(self):
        dao = CategoryDao()
        return dao

    def test_category_dao_instance(self, category_dao):
        assert isinstance(category_dao, CategoryDao)
        assert isinstance(category_dao, BaseDao)

    def test_save_method(self, category_dao, category_instance):
        category_saved = category_dao.save(category_instance)
        assert category_saved.id is not None
        assert category_saved.name == category_instance.name
        assert category_saved.description == category_instance.description
        category_dao.delete(category_saved)

    @pytest.mark.parametrize("fake_category", [
        'string', 1, 1.0, [1, 2, 3]
    ])
    def test_fail_save_method(self, category_dao, fake_category):
        with pytest.raises(UnmappedInstanceError):
            category_saved = category_dao.save(fake_category)

    def test_read_by_id_method(self, category_dao, category_instance):
        category_saved = category_dao.save(category_instance)
        category_read = category_dao.read_by_id(category_saved.id)
        assert isinstance(category_read, Category)
        category_dao.delete(category_saved)

    @pytest.mark.parametrize("fake_category", [
        'string', 1.0, [1, 2, 3]
    ])
    def test_fail_read_by_id_method(self, category_dao, fake_category):
        with pytest.raises(TypeError):
            category_read = category_dao.read_by_id(fake_category)

    def test_read_all_method(self, category_dao):
        category_list = category_dao.read_all()
        assert isinstance(category_list, list)
        assert all(isinstance(item, Category) for item in category_list)

    def test_delete_method(self, category_dao, category_instance):
        category_saved = category_dao.save(category_instance)
        category_read = category_dao.read_by_id(category_saved.id)
        category_dao.delete(category_read)
        category_read = category_dao.read_by_id(category_saved.id)
        assert category_read is None

    @pytest.mark.parametrize("fake_category", [
        'string', 1, 1.0, [1, 2, 3]
    ])
    def test_not_delete(self, category_dao, fake_category):
        with pytest.raises(UnmappedInstanceError):
            category_dao.delete(fake_category)
