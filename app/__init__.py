from flask import Flask
from app.config import Config
from app.database.mongodb import init_database
from app.controllers.home_controller import home_bp
from app.controllers.history_controller import history_bp
from app.controllers.articles_controller import articles_bp
from app.controllers.categories_controller import categories_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_database(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(articles_bp)
    app.register_blueprint(categories_bp)

    return app