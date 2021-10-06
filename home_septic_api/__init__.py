import os
import werkzeug
from flask.scaffold import _endpoint_from_view_func
from werkzeug.utils import cached_property
import flask

flask.helpers._endpoint_from_view_func = _endpoint_from_view_func
# Workaround for incompatible versions: https://github.com/noirbizarre/flask-restplus/issues/777
werkzeug.cached_property = cached_property

from flask import Flask
from .rest.blueprint import septic_bp


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("../config.py", silent=False)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(septic_bp)

    # Disable "extra" field in Swagger doc
    app.config["RESTPLUS_MASK_SWAGGER"] = False

    return app
