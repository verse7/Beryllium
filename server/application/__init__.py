from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

""" 
This is the main application module
"""

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """ Initialize the core app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize plugins
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        # routes
        from . import routes

        # registering blueprints
        from api import api_routes
        app.register_blueprint(api_routes.api_bp)

        return app


# app.config['SECRET_KEY'] = 'cfafc8101c9003bd9eb9172d65b098b1'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False