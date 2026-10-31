from bson import ObjectId
from bson.errors import InvalidId

from app.database.mongodb import get_database


class EditionModel:

    @staticmethod
    def collection():
        return get_database()["editions"]

    @staticmethod
    def get_all():
        return list(
            EditionModel.collection().find().sort("year", -1)
        )

    @staticmethod
    def get_upcoming():
        return EditionModel.collection().find_one(
            {"is_upcoming": True},
            sort=[("date", 1)]
        )

    @staticmethod
    def get_by_id(edition_id):
        try:
            return EditionModel.collection().find_one(
                {"_id": ObjectId(edition_id)}
            )
        except (InvalidId, TypeError):
            return None

    @staticmethod
    def create(data):
        return EditionModel.collection().insert_one(data)

    @staticmethod
    def update(edition_id, data):
        try:
            return EditionModel.collection().update_one(
                {"_id": ObjectId(edition_id)},
                {"$set": data}
            )
        except (InvalidId, TypeError):
            return None

    @staticmethod
    def delete(edition_id):
        try:
            return EditionModel.collection().delete_one(
                {"_id": ObjectId(edition_id)}
            )
        except (InvalidId, TypeError):
            return None