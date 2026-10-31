from app.models.article_model import ArticleModel


class ArticleService:

    @staticmethod
    def get_published_articles():
        return ArticleModel.get_published()

    @staticmethod
    def get_all_articles():
        return ArticleModel.get_all()

    @staticmethod
    def get_article_details(article_id):
        return ArticleModel.get_by_id(article_id)