import pytest
from app import create_app, db
from app.models import Toy, Game


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def init_database(app):
    with app.app_context():
        # Create test toys
        toy1 = Toy(name="Test Toy 1", description="Description 1", max_age=5)
        toy2 = Toy(name="Test Toy 2", description="Description 2", max_age=10)
        db.session.add_all([toy1, toy2])

        # Create test games
        game1 = Game(
            title="Test Game 1", description="Game Description 1", player_count=2
        )
        game2 = Game(
            title="Test Game 2", description="Game Description 2", player_count=4
        )
        db.session.add_all([game1, game2])

        db.session.commit()

    yield

    with app.app_context():
        db.session.remove()
        db.drop_all()
