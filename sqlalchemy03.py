import os
import sqlite3
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('sqlite:///C:\\Users\\lucas\\Desktop\\PycharmProjects\\python_learning\SQL\\aeroporto.sqlite')
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print("Flight {} {} to {}, {} minutes".format(flight.id, flight.origin, flight.destination, flight.duration))
if __name__ == '__main__': #perguntar ao Luke porque isso não printou sem precisar chamar a função novamente
    main()
flight_id = int(input("\nFlight ID: "))#uso dos : pra placeholder, pequena dúvida ainda
flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
if flight is None:
    print("Erro, no such flight.")
    #return

passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id", {"flight_id": flight_id}).fetchall()
print("\nPassengers:")
for passenger in passengers:
    print(passenger.name)
if len(passengers) == 0:
    print("No passengers.")
