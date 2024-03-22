#!/usr/bin/python3
"""Creates the State name passed a new arg."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    se = Session()

    new_State = State(name='California')
    new_City = City(name='San Francisco')
    new_State.cities.append(new_City)

    se.add(new_State)
    se.add(new_City)
    se.commit()
