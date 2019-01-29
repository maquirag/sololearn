import sqlite3

with sqlite3.connect(':memory:') as memdb:
    cur = memdb.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='info'")
    if not cur.fetchall():
        print("Table does not exist. Creating table...")
        cur.execute("CREATE TABLE info (name TEXT, age INTEGER)")
    print("Inserting some rows...")
    newrows = [('Joe', 15), ('Jack', 22)]
    cur.executemany("INSERT INTO info VALUES (?, ?)", newrows)
    memdb.commit()
    print("Querying the table...")
    cur.execute("SELECT * FROM info")
    print(*cur.fetchall(), sep='\n')