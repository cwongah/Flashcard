#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_cors import CORS

# Local imports
# from config import app, db, api
from config import *
from models import User

# Views go here!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

if __name__ == '__main__':
    app.run(port=5555, debug=True)
