from database import create_tables, add_book, view_books, add_member, view_members, borrow_book, view_borrowed_books

create_tables()
print("Database initialized")



# title = input("Enter title: ")
# author = input("Enter author: ")
# year = int(input("Enter year: "))

# add_book(title, author, year)
# print ("Book added succesfully")

# books = view_books()
# for row in books:
#         print(f"{row[0]} {row[1]}")

# add_member("John", "john@gmail.com")
# print("Member added")
# print(view_members())

borrowed_books = view_borrowed_books()
for title, member, borrow_date in borrowed_books:
    print(f"{title}\nBorrowed by: {member}\n{borrow_date}")




