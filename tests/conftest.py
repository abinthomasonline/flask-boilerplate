import pytest
from app import create_app, db
from app.models import Toy, Game


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def init_database(app):
    with app.app_context():
        db.create_all()
        # Remove the test data creation, as we now have initial data loaded in create_app()
        yield db
        db.drop_all()
