from models.base_model import BaseModel, Base
import pytest


class TestBaseModel:
    @pytest.fixture
    def base_model_instance(self):
        return BaseModel()

    def test_abstract(self, base_model_instance):
        assert base_model_instance.__abstract__ is True

    def test_base_model_instance(self, base_model_instance):
        assert isinstance(base_model_instance, Base)
        assert isinstance(base_model_instance, BaseModel)
