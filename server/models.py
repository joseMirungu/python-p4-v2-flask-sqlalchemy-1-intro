# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Create a metadata object for the database schema
metadata = MetaData()

# Create the Flask-SQLAlchemy extension object
db = SQLAlchemy(metadata=metadata)

# Define a model class by inheriting from db.Model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
