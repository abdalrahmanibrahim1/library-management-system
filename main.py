from database import create_tables, add_book, view_books

create_tables()
print("Database initialized")



# title = input("Enter title: ")
# author = input("Enter author: ")
# year = int(input("Enter year: "))

# add_book(title, author, year)
# print ("Book added succesfully")

books = view_books()
for row in books:
        print(f"{row[0]} {row[1]}")
