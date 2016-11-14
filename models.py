from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from app import db
import datetime

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.


class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password


class Event(Base):
    __tablename__ = 'Events'

    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(120))
    published_at = db.Column(db.DateTime)


    def __init__(self, event=None, published_at=None):
        self.name = event
        self.published_at = datetime.datetime.now()


# Create tables.
Base.metadata.create_all(bind=engine)
