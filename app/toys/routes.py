from flask import jsonify, request
from . import toys_bp
from ..models import Toy
from .. import db

@toys_bp.route('/toys', methods=['GET'])
def get_toys():
    toys = Toy.query.all()
    return jsonify([{'id': t.id, 'name': t.name} for t in toys])

@toys_bp.route('/toys', methods=['POST'])
def create_toy():
    data = request.json
    new_toy = Toy(name=data['name'], description=data['description'], max_age=data['max_age'])
    db.session.add(new_toy)
    db.session.commit()
    return jsonify({'id': new_toy.id, 'name': new_toy.name, 'description': new_toy.description, 'max_age': new_toy.max_age}), 201

@toys_bp.route('/toys/<int:toy_id>', methods=['GET'])
def get_toy(toy_id):
    toy = db.session.get(Toy, toy_id)
    if toy is None:
        return jsonify({'error': 'Toy not found'}), 404
    return jsonify({'id': toy.id, 'name': toy.name, 'description': toy.description, 'max_age': toy.max_age})

@toys_bp.route('/toys/<int:toy_id>', methods=['PUT'])
def update_toy(toy_id):
    toy = db.session.get(Toy, toy_id)
    if toy is None:
        return jsonify({'error': 'Toy not found'}), 404
    data = request.json
    toy.name = data['name']
    toy.description = data['description']
    toy.max_age = data['max_age']
    db.session.commit()
    return jsonify({'id': toy.id, 'name': toy.name, 'description': toy.description, 'max_age': toy.max_age})

@toys_bp.route('/toys/<int:toy_id>', methods=['DELETE'])
def delete_toy(toy_id):
    toy = db.session.get(Toy, toy_id)
    if toy is None:
        return jsonify({'error': 'Toy not found'}), 404
    db.session.delete(toy)
    db.session.commit()
    return '', 204