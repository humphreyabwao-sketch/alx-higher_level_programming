#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. This script is safe from
MySQL injections."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query with proper escaping to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
