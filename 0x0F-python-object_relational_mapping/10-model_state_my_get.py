#!/usr/bin/python3
"""Name pased in the dtaabase in the argu."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    s = Session()

    st = s.query(State).filter(State.name == (state_name,))
    try:
        print(st[0].id)
    except IndexError:
        print("Not found")
