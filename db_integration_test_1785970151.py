import sqlite3


def lookup(conn, user_id):
    # SQL injection: user input interpolated into the query
    return conn.execute(f"SELECT * FROM users WHERE id = {user_id}").fetchall()
