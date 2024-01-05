from sqlalchemy_serializer import SerializerMixin
# from flask_restful import Api, Resource
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import *

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    #Attributes
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.Text)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    #Relationships
    flashcards = db.relationship('Flashcard', backref = 'user')
    collections = db.relationship('Collection', backref = 'user')

    #Serialization

class Flashcard(db.Model, SerializerMixin):
    __tablename__ = 'flashcards'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column (db.DateTime, onupdate=db.func.now())

    #Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'))

    #Serialization

class Collection(db.Model, SerializerMixin):
    __tablename__ = 'collections'

    #Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column (db.DateTime, onupdate=db.func.now())

    #Relationships
    flashcards = db.relationship('Flashcard', backref = 'collection')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #Serialization

# Models Template
    # class (db.Model, SerializerMixin):
    #     __tablename__ = ''

    #     #Attributes
    #     id = db.Column(db.Integer, primary_key=True)
    #     created_at = db.Column(db.DateTime, server_default=db.func.now())
    #     updated_at = db.Column (db.DateTime, onupdate=db.func.now())

    #     #Relationships

    #     #Serialization