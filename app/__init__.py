""" init file for app """
import locale
from flask import Flask
from app.api import API_BP
from app.web.views import WEB_BP
from app.models import db
from flask_migrate import Migrate

def create_app(test_config=None):
    """ init app """
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config')
    else:
        # load the test config if passed
        app.config.from_mapping(test_config)

    # init libraries
    db.init_app(app)
    migrate = Migrate(app, db)

    app.config['BUNDLE_ERRORS'] = True

    # register blueprints
    app.register_blueprint(API_BP, url_prefix='/api')
    app.register_blueprint(WEB_BP, url_prefix='')

    return app
