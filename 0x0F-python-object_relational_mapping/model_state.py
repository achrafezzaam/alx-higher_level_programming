#!/usr/bin/python3
""" Define the state model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class inheriting from Base class

    Args:
        __tablename__(str): The name of the table
        id(int)           : The table's primary key
        name(str)         : The state name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
