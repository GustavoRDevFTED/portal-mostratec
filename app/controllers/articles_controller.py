from flask import Blueprint, render_template
from app.services.content_service import get_articles

articles_bp = Blueprint("articles", __name__)

@articles_bp.get("/artigos")
def index():
    articles = []
    try:
        articles = get_articles()
    except RuntimeError:
        pass
    return render_template("articles.html", articles=articles)