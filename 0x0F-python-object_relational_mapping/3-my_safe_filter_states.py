#!/usr/bin/python3
"""
Filter states by user input safe from MySQL injections!
It takes in an argument and displays all values in the states table
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3])
    cursor = db.cursor()
    # BINARY ->  only names with the exact case are printed
    # %s is a placeholder for the search term
    query = "SELECT * FROM states WHERE states.name \
                LIKE BINARY %s ORDER BY states.id ASC"
    cursor.execute(query, (argv[4],))
    results = cursor.fetchall()
    for state in results:
        print(state)
    cursor.close()
    db.close()
