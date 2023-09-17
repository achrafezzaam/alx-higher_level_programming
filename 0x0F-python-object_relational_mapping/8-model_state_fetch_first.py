#!/usr/bin/python3
""" List the first State object from the database hbtn_0e_6_usa """

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))
    session.close()
