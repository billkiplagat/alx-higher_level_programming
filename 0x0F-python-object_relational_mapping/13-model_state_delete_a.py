#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    delete_with_a = session.query(State).filter(State.name.like('%a%')).all()
    if delete_with_a:
        for state in delete_with_a:
            session.delete(state)
        session.commit()
    else:
        print("Data with a not found.")

    session.close()
