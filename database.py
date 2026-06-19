import sqlite3
from datetime import date, timedelta

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

def add_borrow_record(book_id, member_id, borrow_date, return_date):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    insert_query = """
    INSERT INTO borrow_records (book_id, member_id, borrow_date, return_date) 
    VALUES ( ?, ?, ?, ?)
    """

    cursor.execute(insert_query, (book_id, member_id, borrow_date, return_date))

    conn.commit()
    conn.close()

def update_availability(book_id, available):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    update_query = """
        UPDATE books
        SET available = ?
        WHERE id = ?
    """

    cursor.execute(update_query, (available, book_id))

    conn.commit()
    conn.close()

def borrow_book(book_id, member_id):
    
    books = view_books()
    members = view_members()
    books_ids = [row[0] for row in books]
    members_ids =  [row[0] for row in members]
    selected_book = None

    for book in books:
        if book[0] == int(book_id):
            selected_book = book
            break

    if int(book_id) not in books_ids:
        print("Invalid book id")
        return
    elif int(member_id) not in members_ids:
        print("Invalid member id")
        return
    elif selected_book[4] == 0:
        print("The book is currently unavailable")
        return
    else:
        add_borrow_record(book_id, member_id, date.today(), date.today()+timedelta(days=10))
        update_availability(book_id, 0)

def view_borrowed_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT b.title, 
           m.name,
           br.borrow_date
    FROM borrow_records AS br
    JOIN books AS b
    ON br.book_id = b.id
    JOIN members AS m
    ON br.member_id = m.id
    """)

    result = cursor.fetchall()

    conn.close()

    return result