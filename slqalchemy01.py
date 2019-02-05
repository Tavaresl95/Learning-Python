import os
import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('sqlite:///C:\\Users\\lucas\PycharmProjects\\python_learning\\SQL\\aeroporto.sqlite')
db = scoped_session(sessionmaker(bind=engine))



def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")

if __name__ == "__main__":
    main()
