from flask import Blueprint

septic_bp = Blueprint('septic_api', __name__)
 
 # a simple page that says hello
@septic_bp.route('/hello')
def hello():
    return 'Hello, World!'