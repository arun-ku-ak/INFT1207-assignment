# Name: Arun Kumar, Nukul Nanchahal, Arun Kumar
# Date: February 7, 2025
# Description: Adding, Listing, Searching, Deleting, and Updating books.

import csv

# Function to add a book to the CSV file
def add_book(title, author, year):
    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])


# Function to retrieve and display all books
def list_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")


# Function to search for a book by title.
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[0].lower() == title.lower():
                print(f"Book found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")
                found = True
                break
        if not found:
            print("Book not found.")


# Function to delete a book by title
def delete_book(title):
    rows = []
    found = False
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('books.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0].lower() == title.lower():
                found = True
                print(f"Deleted book: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")
            else:
                writer.writerow(row)

    if not found:
        print("Book not found to delete.")


# Function to update a book by title
def update_book(old_title, new_title, new_author, new_year):
    rows = []
    found = False
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('books.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0].lower() == old_title.lower():
                found = True
                writer.writerow([new_title, new_author, new_year])
                print(f"Updated book: {new_title}, {new_author}, {new_year}")
            else:
                writer.writerow(row)

    if not found:
        print("Book not found to update.")


# Menu function to allow user interaction
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. List all books")
        print("3. Search for a book")
        print("4. Delete a book")
        print("5. Update a book")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == "2":
            list_books()
        elif choice == "3":
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == "4":
            title = input("Enter book title to delete: ")
            delete_book(title)
        elif choice == "5":
            old_title = input("Enter book title to update: ")
            new_title = input("Enter new book title: ")
            new_author = input("Enter new author name: ")
            new_year = input("Enter new year of publication: ")
            update_book(old_title, new_title, new_author, new_year)
        elif choice == "6":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    menu()