import sqlite3

def create_tables():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON") # Enable foreign key enforcement in SQLite


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER NOT NULL,
        available INTEGER DEFAULT 1
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrow_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        member_id INTEGER,
        borrow_date TEXT,
        return_date TEXT,
                   
        FOREIGN KEY(book_id) REFERENCES books(id),
        FOREIGN KEY(member_id) REFERENCES members(id)
    )
    """)
    
    conn.commit()
    conn.close()

def add_book(title, author, year):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    insert_query = """
    INSERT INTO books (title, author, year) 
    VALUES ( ?, ?, ?)
    """

    cursor.execute(insert_query, (title, author, year))

    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    conn.close()

    return result
    
def add_member(name, email):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    insert_query = """
    INSERT INTO members (name, email) 
    VALUES ( ?, ?)
    """

    cursor.execute(insert_query, (name, email))

    conn.commit()
    conn.close() 

def view_members():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    result = cursor.fetchall()
    conn.close()

    return result