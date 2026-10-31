from bson import ObjectId
from bson.errors import InvalidId

from app.database.mongodb import get_database


class ArticleModel:

    @staticmethod
    def collection():
        return get_database()["articles"]

    @staticmethod
    def get_all():
        return list(
            ArticleModel.collection().find().sort(
                "created_at", -1
            )
        )

    @staticmethod
    def get_published():
        return list(
            ArticleModel.collection().find(
                {"published": True}
            ).sort("created_at", -1)
        )

    @staticmethod
    def get_by_id(article_id):
        try:
            return ArticleModel.collection().find_one(
                {"_id": ObjectId(article_id)}
            )
        except (InvalidId, TypeError):
            return None

    @staticmethod
    def create(data):
        return ArticleModel.collection().insert_one(data)

    @staticmethod
    def update(article_id, data):
        try:
            return ArticleModel.collection().update_one(
                {"_id": ObjectId(article_id)},
                {"$set": data}
            )
        except (InvalidId, TypeError):
            return None