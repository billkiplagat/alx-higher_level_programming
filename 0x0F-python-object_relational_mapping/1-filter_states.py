#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
It takes 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    results = cursor.fetchall()
    for state in results:
        print(state)
    cursor.close()
    db.close()
