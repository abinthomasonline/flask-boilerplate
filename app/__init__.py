from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path="/static", static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)

    from .toys import toys_bp
    from .games import games_bp
    from .main import main_bp

    app.register_blueprint(toys_bp)
    app.register_blueprint(games_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
