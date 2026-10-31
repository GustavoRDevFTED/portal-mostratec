from flask import Blueprint, render_template
from app.services.content_service import get_categories

categories_bp = Blueprint("categories", __name__)

@categories_bp.get("/categorias")
def index():
    categories = []
    try:
        categories = get_categories()
    except RuntimeError:
        pass
    return render_template("categories.html", categories=categories)