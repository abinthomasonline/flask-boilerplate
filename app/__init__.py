from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from werkzeug.middleware.proxy_fix import ProxyFix
from app.utils import RetryingQuery
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
import json
import os

db = SQLAlchemy(query_class=RetryingQuery)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.close()


def create_app():
    app = Flask(__name__, static_url_path="/static", static_folder="static")
    app.config.from_object(Config)

    # Setup ProxyFix for production
    if not app.debug and not app.testing:
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    db.init_app(app)

    from .toys import toys_bp
    from .games import games_bp
    from .main import main_bp

    app.register_blueprint(toys_bp)
    app.register_blueprint(games_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

        # Load initial data for toys and games (for demo purposes)
        load_initial_data()

    return app


def load_initial_data():
    from .models import Toy, Game

    # Load toys
    if Toy.query.count() == 0:
        with open(os.path.join(os.path.dirname(__file__), "toys_init.json")) as f:
            toys_data = json.load(f)
        for toy_data in toys_data:
            toy = Toy(**toy_data)
            db.session.add(toy)

    # Load games
    if Game.query.count() == 0:
        with open(os.path.join(os.path.dirname(__file__), "games_init.json")) as f:
            games_data = json.load(f)
        for game_data in games_data:
            game = Game(**game_data)
            db.session.add(game)

    db.session.commit()


# Comment: The above function loads initial data for demo purposes.
# You can remove or modify this for real-world use.
