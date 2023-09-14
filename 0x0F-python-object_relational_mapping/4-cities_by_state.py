#!/usr/bin/python3
"""
Lists all cities from the database using foreign key
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id"
    cursor.execute(query)

    results = cursor.fetchall()
    for cities in results:
        print(cities)
    cursor.close()
    db.close()
