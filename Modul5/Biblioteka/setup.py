import sqlite3


with sqlite3.connect('librady.db') as conn:
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100) UNIQUE NOT NULL,
            author VARCHAR(100)
            ) ''')
    conn.commit()
