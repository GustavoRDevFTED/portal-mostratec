from bson import ObjectId
from bson.errors import InvalidId

from app.database.mongodb import get_database


class CategoryModel:

    @staticmethod
    def collection():
        return get_database()["categories"]

    @staticmethod
    def get_all():
        return list(
            CategoryModel.collection().find().sort("name", 1)
        )

    @staticmethod
    def get_by_id(category_id):
        try:
            return CategoryModel.collection().find_one(
                {"_id": ObjectId(category_id)}
            )
        except (InvalidId, TypeError):
            return None

    @staticmethod
    def create(data):
        return CategoryModel.collection().insert_one(data)