from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.utils import RetryingQuery
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection


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
