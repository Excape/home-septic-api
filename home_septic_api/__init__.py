import os

from flask import Flask
from .routes import septic_bp



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # create and configure the app
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    app.register_blueprint(septic_bp)

    return app
