import json

def test_get_toys(client, init_database):
    response = client.get('/toys')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert all(key in data[0] for key in ['id', 'name'])

def test_create_toy(client):
    response = client.post('/toys', json={
        'name': 'New Toy',
        'description': 'New Description',
        'max_age': 8
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'New Toy'
    assert data['description'] == 'New Description'
    assert data['max_age'] == 8

def test_get_toy(client, init_database):
    response = client.get('/toys/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Test Toy 1'

def test_update_toy(client, init_database):
    response = client.put('/toys/1', json={
        'name': 'Updated Toy',
        'description': 'Updated Description',
        'max_age': 7
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Updated Toy'
    assert data['description'] == 'Updated Description'
    assert data['max_age'] == 7

def test_delete_toy(client, init_database):
    response = client.delete('/toys/1')
    assert response.status_code == 204
    response = client.get('/toys/1')
    assert response.status_code == 404