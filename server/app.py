#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask, make_response
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_cors import CORS

# Local imports
# from config import app, db, api
from config import *
from models import User, Collection, Flashcard

# Views go here!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

class Users(Resource):
    def get(self):
        users = User.query.all()
        users_dict_list = [user.to_dict() for user in users]
        return make_response(users_dict_list, 200)
api.add_resource(Users, '/users')

class UsersById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({'error': 'User not found'}, 404)
        return make_response(user.to_dict(), 200)
api.add_resource(UsersById, '/users/<int:id>')

class Collections(Resource):
    def get(self):
        collections = Collection.query.all()
        collections_dict_list = [collection.to_dict() for collection in collections]
        return make_response(collections_dict_list, 200)
api.add_resource(Collections, '/collections')

class CollectionById(Resource):
    def get(self, id):
        collection = Collection.query.filter_by(id=id).first()
        if not collection:
            return make_response({'error': 'Collection not found'}, 404)
        return make_response(collection.to_dict(), 200)
api.add_resource(CollectionById, '/collections/<int:id>')

class Flashcards(Resource):
    def get(self):
        flashcards = Flashcard.query.all()
        flashcards_dict_list = [flashcard.to_dict() for flashcard in flashcards]
        return make_response(flashcards_dict_list, 200)
api.add_resource(Flashcards, '/flashcards')

class FlashcardsById(Resource):
    def get(self, id):
        flashcard = Collection.query.filter_by(id = id).first()
        if not flashcard:
            return make_response({'error': 'Flashcard not found'}, 404)
        return make_response(flashcard.to_dict(), 200)
api.add_resource(FlashcardsById, '/flashcards/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
