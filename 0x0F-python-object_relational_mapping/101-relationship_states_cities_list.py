#!/usr/bin/python3
"""Define the state of the obj with the newname passed as argu."""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    for ins in ses.query(State).order_by(State.id):
        print(ins.id, ins.name, sep=": ")
        for ins_city in ins.cities:
            print("    ", end="")
            print(ins_city.id, ins_city.name, sep=": ")
