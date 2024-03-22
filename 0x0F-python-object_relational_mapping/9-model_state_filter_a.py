#!/usr/bin/python3
"""Lists all State objects that contain the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    s = Session()

    st = s.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for sta in st:
        print("{}: {}".format(sta.id, sta.name))
