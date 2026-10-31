from app.models.project_model import ProjectModel
from app.models.team_model import TeamModel
from app.models.category_model import CategoryModel


class ProjectService:

    @staticmethod
    def get_all_projects():
        return ProjectModel.get_all()

    @staticmethod
    def get_featured_projects():
        return ProjectModel.get_featured()

    @staticmethod
    def get_winning_projects():
        return ProjectModel.get_winners()

    @staticmethod
    def get_project_details(project_id):
        project = ProjectModel.get_by_id(project_id)

        if not project:
            return None

        team_id = project.get("team_id")
        category_id = project.get("category_id")

        project["team"] = (
            TeamModel.get_by_id(team_id)
            if team_id else None
        )

        project["category"] = (
            CategoryModel.get_by_id(category_id)
            if category_id else None
        )

        return project