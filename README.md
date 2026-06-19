# Library Management System

## Overview

A command-line Library Management System built with Python and SQLite.

This project allows users to manage books, library members, and borrowing records using a relational database.

The goal of the project was to practice database design, SQL fundamentals, and integrating SQLite with Python.

---

## Features

* Add new books
* View all books
* Add library members
* View all members
* Borrow books
* Return books
* Track borrowing history
* View currently borrowed books

---

## Database Schema

### Books

| Column    | Type    |
| --------- | ------- |
| id        | INTEGER |
| title     | TEXT    |
| author    | TEXT    |
| year      | INTEGER |
| available | INTEGER |

### Members

| Column | Type    |
| ------ | ------- |
| id     | INTEGER |
| name   | TEXT    |
| email  | TEXT    |

### Borrow Records

| Column      | Type    |
| ----------- | ------- |
| id          | INTEGER |
| book_id     | INTEGER |
| member_id   | INTEGER |
| borrow_date | TEXT    |
| return_date | TEXT    |

Relationships are enforced using foreign keys between books, members, and borrow records.

---

## Technologies Used

* Python
* SQLite
* SQL
* Git
* GitHub

---

## What I Learned

Through this project I practiced:

* Creating relational database schemas
* Using foreign keys
* Writing SQL queries
* Using joins
* Performing CRUD operations
* Connecting Python applications to SQLite databases
* Managing project versions with Git and GitHub

---

## Future Improvements

* Interactive command-line menu
* Search books by title or author
* Overdue book tracking
* Due date management
* Data validation and error handling
* Automated testing
