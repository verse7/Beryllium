from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'cfafc8101c9003bd9eb9172d65b098b1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = SQLAlchemy(app)

ma = Marshmallow(app)

from mentorsys import routes