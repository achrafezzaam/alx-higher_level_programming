#!/usr/bin/python3
""" List all City objects from the database hbtn_0e_6_usa """

from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_list = session.query(State, City).join(City).order_by(City.id).all()
    [print("{}: ({}) {}".format(state.name, city.id, city.name))
        for state, city in state_list]
    session.close()
