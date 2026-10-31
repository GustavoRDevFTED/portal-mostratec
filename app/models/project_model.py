from bson import ObjectId
from bson.errors import InvalidId

from app.database.mongodb import get_database


class ProjectModel:

    @staticmethod
    def collection():
        return get_database()["projects"]

    @staticmethod
    def get_all():
        return list(
            ProjectModel.collection().find().sort("name", 1)
        )

    @staticmethod
    def get_featured():
        return list(
            ProjectModel.collection().find(
                {"featured": True}
            ).sort("name", 1)
        )

    @staticmethod
    def get_winners(edition_id=None):
        query = {"is_winner": True}

        if edition_id:
            query["edition_id"] = edition_id

        return list(
            ProjectModel.collection().find(query)
        )

    @staticmethod
    def get_by_edition(edition_id):
        return list(
            ProjectModel.collection().find(
                {"edition_id": edition_id}
            )
        )

    @staticmethod
    def get_by_id(project_id):
        try:
            return ProjectModel.collection().find_one(
                {"_id": ObjectId(project_id)}
            )
        except (InvalidId, TypeError):
            return None

    @staticmethod
    def create(data):
        return ProjectModel.collection().insert_one(data)

    @staticmethod
    def update(project_id, data):
        try:
            return ProjectModel.collection().update_one(
                {"_id": ObjectId(project_id)},
                {"$set": data}
            )
        except (InvalidId, TypeError):
            return None