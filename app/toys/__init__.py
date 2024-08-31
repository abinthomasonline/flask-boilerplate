from flask import Blueprint

toys_bp = Blueprint('toys', __name__)

from . import routes