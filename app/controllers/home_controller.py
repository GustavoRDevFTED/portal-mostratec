from flask import Blueprint, render_template
from app.services.content_service import get_upcoming_edition, get_featured_projects

home_bp = Blueprint("home", __name__)

@home_bp.get("/")
def index():
    edition = None
    projects = []
    try:
        edition = get_upcoming_edition()
        projects = get_featured_projects()
    except RuntimeError:
        pass

    return render_template("home.html", edition=edition, projects=projects)