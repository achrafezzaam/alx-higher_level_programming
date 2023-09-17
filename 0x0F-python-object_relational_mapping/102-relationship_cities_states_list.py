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

    info_list = session.query(City).order_by(City.id).all()
    [print("{}: {} -> {}".format(city.id, city.name, city.state.name))
        for city in info_list]
    session.close()
