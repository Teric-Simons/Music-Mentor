# Add any model classes for Flask-SQLAlchemy here
from flask import Flask
from . import db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class Upload(db.Model):
    __tablename__ = "uploads"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    composer = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    instrument = db.Column(db.String, nullable=False)
    sheet = db.Column(db.String, nullable=False)

    def __init__(self, title, composer, genre, instrument, sheet):
        self.title = title
        self.composer = composer
        self.genre = genre
        self.instrument = instrument
        self.sheet = sheet

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    tutors = db.relationship("Tutors", backref="user")


class Tutors(db.Model):
    __tablename__ = "tutors"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, db.ForeignKey('users.email'))
    instrument = db.Column(db.String)
    language = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    isSuper = db.Column(db.Boolean, default = True)
    countryOfBirth = db.Column(db.String)
    imglink = db.Column(db.String)
    video = db.Column(db.String)




class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String)
    fromm = db.Column(db.String)
    message = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.now)



class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String)
    fromm = db.Column(db.String)
    email_bookee = db.Column(db.String)
    email_booker = db.Column(db.String, db.ForeignKey('users.email'))


    ## references from other relations


    
   