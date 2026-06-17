import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
branch TEXT,
year TEXT,
email TEXT,
phone TEXT
)
''')

conn.close()

print("Database created")

