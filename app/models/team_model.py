from bson import ObjectId
from bson.errors import InvalidId

from app.database.mongodb import get_database


class TeamModel:

    @staticmethod
    def collection():
        return get_database()["teams"]

    @staticmethod
    def get_all():
        return list(
            TeamModel.collection().find().sort("name", 1)
        )

    @staticmethod
    def get_by_id(team_id):
        try:
            return TeamModel.collection().find_one(
                {"_id": ObjectId(team_id)}
            )
        except (InvalidId, TypeError):
            return None

    @staticmethod
    def create(data):
        return TeamModel.collection().insert_one(data)

    @staticmethod
    def update(team_id, data):
        try:
            return TeamModel.collection().update_one(
                {"_id": ObjectId(team_id)},
                {"$set": data}
            )
        except (InvalidId, TypeError):
            return None