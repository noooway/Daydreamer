import os

from flask import Flask
from . import dreamcatcher as dc


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        HELLO_TEXT="Go to Hell!",
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(dreamcatcher.bp)
    app.add_url_rule('/', endpoint='render_plans')

    return app
