import os
import werkzeug
from flask.scaffold import _endpoint_from_view_func
from werkzeug.utils import cached_property
import flask

flask.helpers._endpoint_from_view_func = _endpoint_from_view_func
# Workaround for incompatible versions: https://github.com/noirbizarre/flask-restplus/issues/777
werkzeug.cached_property = cached_property

from flask import Flask
from .blueprint import septic_bp
from .homecanaryapi import HomeCanaryApi


homecanary_api: HomeCanaryApi = None

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("../config.py", silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    app.register_blueprint(septic_bp)

    homecanary_api = HomeCanaryApi(app.config)

    return app
