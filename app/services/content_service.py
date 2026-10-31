from app.services.edition_service import EditionService
from app.services.project_service import ProjectService
from app.services.article_service import ArticleService
from app.services.category_service import CategoryService


# Home

def get_upcoming_edition():
    return EditionService.get_upcoming_edition()


def get_featured_projects():
    return ProjectService.get_featured_projects()


# History

def get_editions():
    return EditionService.get_all_editions()


def get_all_editions():
    return EditionService.get_all_editions()


def get_projects_for_edition(edition_id):
    return EditionService.get_edition_projects(str(edition_id))


# Articles

def get_articles():
    return ArticleService.get_published_articles()

def get_published_articles():
    return ArticleService.get_published_articles()


# Categories

def get_categories():
    return CategoryService.get_all_categories()


def get_all_categories():
    return CategoryService.get_all_categories()

class ContentService:

    @staticmethod
    def get_home_content():
        return {
            "upcoming_edition": get_upcoming_edition(),
            "featured_projects": get_featured_projects()
        }

    @staticmethod
    def get_history_content():
        return {
            "editions": get_editions()
        }

    @staticmethod
    def get_articles_content():
        return {
            "articles": get_published_articles()
        }

    @staticmethod
    def get_categories_content():
        return {
            "categories": get_all_categories()
        }