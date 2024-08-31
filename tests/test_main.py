def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Toy and Game Store" in response.data


def test_toys_dashboard(client):
    response = client.get("/toys_dashboard")
    assert response.status_code == 200
    assert b"Toys Dashboard" in response.data


def test_games_dashboard(client):
    response = client.get("/games_dashboard")
    assert response.status_code == 200
    assert b"Games Dashboard" in response.data
