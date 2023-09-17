#!/usr/bin/python3
""" Define the city model """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """City class inheriting from Base class

    Args:
        __tablename__(str): The name of the table
        id(int)           : The table's primary key
        name(str)         : The state name
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
