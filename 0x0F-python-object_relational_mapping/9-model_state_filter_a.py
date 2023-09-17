#!/usr/bin/python3
""" List all State objects from the database hbtn_0e_6_usa """

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_list = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    [print("{}: {}".format(state.id, state.name)) for state in state_list]
    session.close()
