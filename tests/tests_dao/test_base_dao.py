from dao.base_dao import BaseDao
from models.base_model import BaseModel
from models.category_model import Category
import pytest


class TestBaseDao:
    @pytest.fixture
    def base_dao_model_instance(self):
        return BaseDao(Category)

    @pytest.fixture
    def base_dao_base_model_instance(self):
        return BaseDao(BaseModel)

    def test_base_dao_instance(self, base_dao_model_instance, base_dao_base_model_instance):
        assert isinstance(base_dao_model_instance, BaseDao)
        assert isinstance(base_dao_base_model_instance, BaseDao)
