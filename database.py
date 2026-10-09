import sqlite3

connection = sqlite3.connect("students.db", check_same_thread=False)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dob TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    course TEXT
)
""")

connection.commit()