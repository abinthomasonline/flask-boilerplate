from flask import jsonify, request
from . import games_bp
from ..models import Game
from .. import db

@games_bp.route('/games', methods=['GET'])
def get_games():
    games = Game.query.all()
    return jsonify([{'id': g.id, 'title': g.title} for g in games])

@games_bp.route('/games', methods=['POST'])
def create_game():
    data = request.json
    new_game = Game(title=data['title'], description=data['description'], player_count=data['player_count'])
    db.session.add(new_game)
    db.session.commit()
    return jsonify({'id': new_game.id, 'title': new_game.title, 'description': new_game.description, 'player_count': new_game.player_count}), 201

@games_bp.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get_or_404(game_id)
    return jsonify({'id': game.id, 'title': game.title, 'description': game.description, 'player_count': game.player_count})

@games_bp.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    game = Game.query.get_or_404(game_id)
    data = request.json
    game.title = data['title']
    game.description = data['description']
    game.player_count = data['player_count']
    db.session.commit()
    return jsonify({'id': game.id, 'title': game.title, 'description': game.description, 'player_count': game.player_count})

@games_bp.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return '', 204