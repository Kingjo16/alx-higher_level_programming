#!/usr/bin/python3
"""Change the stat object of the data base and paas it as argu."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    s = Session()

    state_to_up = s.query(State).filter(State.id == 2).first()
    if state_to_up:
        state_to_up.name = "New Mexico"
        s.commit()
