from mysql.connector import connect, MySQLConnection
from mysql.connector.cursor import MySQLCursor
from typing import Optional

con: Optional[MySQLConnection] = None
cur: Optional[MySQLCursor] = None

def get_db():
    global con, cur

    if con is None:
        print("MySQL Connection")
        con = connect(
            host='127.0.0.1',
            user='root',
            password='1q2w3e',
            database='boomacat',
            charset='utf8'
        )
        cur = con.cursor()

get_db()