from app.models.edition_model import EditionModel
from app.database.mongodb import get_database


class EditionService:

    @staticmethod
    def get_all_editions():
        return EditionModel.get_all()

    @staticmethod
    def get_upcoming_edition():
        return EditionModel.get_upcoming()

    @staticmethod
    def get_edition_details(edition_id):
        edition = EditionModel.get_by_id(edition_id)

        if not edition:
            return None

        edition_id = str(edition["_id"])

        edition["projects"] = EditionService.get_edition_projects(
            edition_id
        )

        edition["winners"] = EditionService.get_edition_winners(
            edition_id
        )

        edition["gallery"] = EditionService.get_edition_gallery(
            edition_id
        )

        return edition

    @staticmethod
    def get_edition_projects(edition_id):
        from app.models.project_model import ProjectModel

        return ProjectModel.get_by_edition(edition_id)

    @staticmethod
    def get_edition_winners(edition_id):
        from app.models.project_model import ProjectModel

        return ProjectModel.get_winners(edition_id)

    @staticmethod
    def get_edition_gallery(edition_id):
        return list(
            get_database()["gallery"].find(
                {"edition_id": edition_id}
            )
        )