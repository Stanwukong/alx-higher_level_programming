#!/usr/bin/python3
"""Lists all states with a name starting with N from thedatabase hbtn_0e_0_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect.(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    data = cur.fetchall
    [print(state) for state in data if state[1][0] == "N"]
    cur.close()
    db.close()
