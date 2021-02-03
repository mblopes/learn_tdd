from dao.base_dao import BaseDao
from models.base_model import BaseModel
from models.category_model import Category
import pytest


class TestBaseDao:
    @pytest.fixture
    def base_dao_instance(self):
        return BaseDao(Category)

    def test_base_dao_instance(self, base_dao_instance):
        assert isinstance(base_dao_instance, BaseDao)
