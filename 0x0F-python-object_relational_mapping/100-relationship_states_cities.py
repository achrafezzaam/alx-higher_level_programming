#!/usr/bin/python3
""" List all State objects from the database hbtn_0e_6_usa """

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

    city = City(name="San Francisco")
    state = State(name="California")
    state.cities.append(city)
    session.add_all([state, city])
    session.commit()
    session.close()
