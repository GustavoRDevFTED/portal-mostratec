from flask import Blueprint, render_template
from app.services.content_service import get_editions, get_projects_for_edition

history_bp = Blueprint("history", __name__)

@history_bp.get("/historia")
def index():
    editions = []
    projects_by_edition = {}
    try:
        editions = get_editions()
        for edition in editions:
            edition_id = str(edition["_id"])
            projects_by_edition[edition_id] = get_projects_for_edition(edition_id)
    except RuntimeError:
        pass

    return render_template(
        "history.html",
        editions=editions,
        projects_by_edition=projects_by_edition
    )