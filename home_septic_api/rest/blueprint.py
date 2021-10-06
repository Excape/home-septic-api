from flask import Blueprint
from flask_restplus import Api
from .homesepticresource import namespace

septic_bp = Blueprint('septic_api', __name__, url_prefix='/api')

api_extension = Api(
    septic_bp,
    title='Home Septic API',
    version='1.0',
    description='API to check what type of sewer system a property has',
    doc='/doc',
    authorizations={
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    }
)

api_extension.add_namespace(namespace)