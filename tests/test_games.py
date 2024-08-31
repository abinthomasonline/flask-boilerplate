import json

def test_get_games(client, init_database):
    response = client.get('/games')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert all(key in data[0] for key in ['id', 'title'])

def test_create_game(client):
    response = client.post('/games', json={
        'title': 'New Game',
        'description': 'New Game Description',
        'player_count': 3
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'New Game'
    assert data['description'] == 'New Game Description'
    assert data['player_count'] == 3

def test_get_game(client, init_database):
    response = client.get('/games/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Test Game 1'

def test_update_game(client, init_database):
    response = client.put('/games/1', json={
        'title': 'Updated Game',
        'description': 'Updated Game Description',
        'player_count': 5
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Updated Game'
    assert data['description'] == 'Updated Game Description'
    assert data['player_count'] == 5

def test_delete_game(client, init_database):
    response = client.delete('/games/1')
    assert response.status_code == 204
    response = client.get('/games/1')
    assert response.status_code == 404