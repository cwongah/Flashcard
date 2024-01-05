#!/usr/bin/env python3

# Standard library imports
import random

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Flashcard, Collection

def make_users():
    User.query.delete()
    users = []
    for i in range(20):
        user = User(
            username = fake.name(),
            password = str(random.randint(0, 10000)),
            email = fake.email()
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

def make_flashcards():
    Flashcard.query.delete()
    flashcards = []
    for i in range(20):
        flashcard = Flashcard(
            question = 'question' + str(i + 1),
            answer = 'answer' + str(i + 1),
            user_id = i + 1,
            collection_id = i + 1
        )
        flashcards.append(flashcard)
    db.session.add_all(flashcards)
    db.session.commit()

def make_collections():
    Collection.query.delete()
    collections = []
    for i in range(20):
        collection = Collection(
            name = 'collection' + str(i + 1),
            user_id = i + 1
        )
        collections.append(collection)
    db.session.add_all(collections)
    db.session.commit()

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        make_users()
        make_flashcards()
        make_collections()