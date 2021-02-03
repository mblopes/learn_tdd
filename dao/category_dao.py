from models.category_model import Category
from dao.base_dao import BaseDao


class CategoryDao(BaseDao):
    def __init__(self):
        self.__model = Category
        super().__init__(self.__model)
