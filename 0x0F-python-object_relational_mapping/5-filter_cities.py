#!/usr/bin/python3
""" List all states from hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id", (sys.argv[4],))
    save = (city[0] for city in cur.fetchall())
    print(", ".join(save))
    cur.close()
    db.close()
