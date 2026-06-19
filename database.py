import sqlite3

def create_table():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER,
        available BOOLEAN
    )
    """)
    conn.commit()
    conn.close()