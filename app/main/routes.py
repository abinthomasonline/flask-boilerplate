from flask import render_template
from . import main_bp

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/toys_dashboard')
def toys_dashboard():
    return render_template('toys_dashboard.html')

@main_bp.route('/games_dashboard')
def games_dashboard():
    return render_template('games_dashboard.html')