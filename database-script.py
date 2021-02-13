import sqlite3

print('connect')
db = sqlite3.connect('customer.db')
cur = db.cursor()
print('create')
cur.execute("""
    CREATE TABLE if not exists customers (
        id INTEGER PRIMARY KEY, user_name text, pin int
    )
    """)

db.commit()