from database import *

create_tables()

def seed_data():
    books = [
        ("Atomic Habits", "James Clear", 2018),
        ("Deep Work", "Cal Newport", 2016),
        ("Clean Code", "Robert C. Martin", 2008),
        ("Python Crash Course", "Eric Matthes", 2015),
        ("The Pragmatic Programmer", "Andrew Hunt", 1999),
        ("Designing Data-Intensive Applications", "Martin Kleppmann", 2017),
        ("Introduction to Algorithms", "CLRS", 2009),
        ("The Hobbit", "J.R.R. Tolkien", 1937),
        ("1984", "George Orwell", 1949),
        ("To Kill a Mockingbird", "Harper Lee", 1960),
    ]

    for title, author, year in books:
        add_book(title, author, year)

    members = [
        ("Ahmad Ali", "ahmad@example.com"),
        ("Sara Khaled", "sara@example.com"),
        ("Omar Hasan", "omar@example.com"),
        ("Layla Nasser", "layla@example.com"),
        ("Yousef Taha", "yousef@example.com"),
        ("Mariam Saleh", "mariam@example.com"),
        ("Khaled Mansour", "khaled@example.com"),
        ("Nour Sami", "nour@example.com"),
        ("Zaid Hamdan", "zaid@example.com"),
        ("Hana Fares", "hana@example.com"),
        ("Ereen Twal", "ereentwal@example.com"),
    ]

    for name, email in members:
        add_member(name, email)

    borrow_records = [
        (1, 1, "2024-01-01"),
        (2, 2, "2024-01-03"),
        (3, 3, "2024-01-05"),
        (4, 4, "2024-01-07"),
        (5, 5, "2024-01-09"),
        (6, 6, "2024-01-11"),
        (7, 7, "2024-01-13"),
        (8, 8, "2024-01-15"),
        (9, 9, "2024-01-17"),
        (10, 10, "2024-01-19"),
    ]

    for book_id, member_id, borrow_date in borrow_records:
        add_borrow_record(book_id, member_id, borrow_date)

    print("Sample data added successfully.")


def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. View books")
        print("3. Add member")
        print("4. View members")
        print("5. Borrow book")
        print("6. Return book")
        print("7. View borrowed books")
        print("8. Add sample data")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            add_book(title, author, year)

        elif choice == "2":
            print(view_books())

        elif choice == "3":
            name = input("Name: ")
            email = input("Email: ")
            add_member(name, email)

        elif choice == "4":
            print(view_members())

        elif choice == "5":
            book_id = int(input("Book ID: "))
            member_id = int(input("Member ID: "))
            borrow_date = input("Borrow date YYYY-MM-DD: ")
            add_borrow_record(book_id, member_id, borrow_date)

        elif choice == "6":
            book_id = int(input("Book ID: "))
            member_id = int(input("Member ID: "))
            return_date = input("Return date YYYY-MM-DD: ")
            return_book(book_id, member_id, return_date)

        elif choice == "7":
            print(view_borrowed_books())

        elif choice == "8":
            seed_data()

        elif choice == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


menu()