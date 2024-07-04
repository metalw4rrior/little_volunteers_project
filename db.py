import sqlite3 as sl

def setup_database():
    con = sl.connect('humans2.db')
    with con:
        data = con.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='users'")
        for row in data:
            if row[0] == 0:
                con.execute("""
                    CREATE TABLE users (
                        name VARCHAR PRIMARY KEY,
                        inn INTEGER,
                        passport VARCHAR,
                        snils VARCHAR,
                        birthday DATE,
                        role VARCHAR
                    );""")

def get_volunteer_names():
    namelist = []
    con = sl.connect('humans2.db')
    with con:
        data = con.execute("SELECT name FROM users")
        for row in data:
            namelist.append(row[0])
    return namelist

def get_volunteer_data_by_role(role):
    con = sl.connect('humans2.db')
    with con:
        data = con.execute(f"SELECT * FROM users WHERE role LIKE '{role}'")
        return data.fetchall()
