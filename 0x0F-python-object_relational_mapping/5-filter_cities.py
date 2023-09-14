#!/usr/bin/python3
"""
Filter cities by state input safe from MySQL injections!
takes in the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    cursor = db.cursor()

    query = "SELECT cities.name FROM cities JOIN states ON \
             cities.state_id = states.id where states.name = %s"
    cursor.execute(query, (argv[4], ))

    results = cursor.fetchall()
    cities = []
    for city in results:
        cities.append(city[0])
    print(", ".join(cities))
    cursor.close()
    db.close()
