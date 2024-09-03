def test_app_creation(app):
    assert app is not None
    assert app.config["TESTING"] == True


def test_db_initialization(app, init_database):
    with app.app_context():
        from app.models import Toy, Game

        assert Toy.query.count() == 10  # Changed from 2 to 10
        assert Game.query.count() == 10  # Changed from 2 to 10
