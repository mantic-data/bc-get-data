"""Contain the engine to create the connection to the database."""

from sqlalchemy import create_engine


DATABASE = "./database.db"

engine = create_engine(f"sqlite:///{DATABASE}", echo=True)
