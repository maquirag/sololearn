# Using sqlite3 you can practice SQL with Python!
import sqlite3

# Opening an in-memory (temporary) database.
# You can also provide a filename as parameter (usually 'something.db')
with sqlite3.connect(':memory:') as memdb:
    # A cursor is used to iterate through data
    cur = memdb.cursor()
    # Checking if table already exists (in this case obviously not)
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='info'")
    if not cur.fetchall():
        print("Table does not exist. Creating table...")
        cur.execute("CREATE TABLE info (name TEXT, age INTEGER)")
    # The recommended way to insert rows, is passing a tuple to cursor.execute()
    # or passing a list of tuples to cursor.executemany()
    print("Inserting some rows...")
    newrows = [('Joe', 15), ('Jack', 22)]
    cur.executemany("INSERT INTO info VALUES (?, ?)", newrows)
    # Commiting the changes will save the database (if it is a file in the system)
    memdb.commit()
    # To query data, execute a SELECT statement on the cursor
    print("Querying the table...")
    cur.execute("SELECT * FROM info")
    # cursor.fetchone() will get one row from the result set as a tuple
    # cursor.fetchall() will get a list of tuples with all rows in the result set
    print(*cur.fetchall(), sep='\n')