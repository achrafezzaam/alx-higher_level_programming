#!/usr/bin/python3
""" List all City objects from the database hbtn_0e_6_usa """

from relationship_state import Base, State
from relationship_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)

    state_list = session.query(State).order_by(State.id).all()
    for state in state_list:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
