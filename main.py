from database import create_tables, add_book

create_tables()
print("Database initialized")



title = input("Enter title: ")
author = input("Enter author: ")
year = int(input("Enter year: "))

add_book(title, author, year)


print ("Book added succesfully")
