# If the scope of this program is ever expanded to increase the security risk of the data in the database then the current programming will be inappropriate.
# Currently the data in the database is considered to be public.

import mysql.connector

bookstore_database = mysql.connector.connect(
    host = "localhost",
    user = "code_reviewer",
    password = "code123",
    database = "bookstore"
    )

# Add validation for title and author. Improve validation for quantity.

def valid_title(title):
    pass

def valid_author():
    pass

def valid_qty(quantity):
    try:
        quantity = int(quantity)
        return True
    except:
        print("You have not entered a valid quantity. This must be a numeral. Please try again. ")
        return False

def enter_book():
    title = input("Please enter the title of the book that you wish to enter: ")
    author = input("Please enter the name of the author that you wish to enter: ")
    qty = input("Please enter the quantity of stock of the book that you wish to enter: ")
    if valid_qty(qty) == True:
        sql = "INSERT INTO books(title, author, qty) VALUES (%s,%s,%s)"
        values = title, author, qty
        cursor = bookstore_database.cursor()
        cursor.execute(sql, values)
        bookstore_database.commit()
        cursor.close() 


def delete_book_by_title(title_to_delete):
    if search_specific_book(title_to_delete) != None:
        cursor = bookstore_database.cursor()
        cursor.execute(f"DELETE FROM books WHERE (title = '{title_to_delete}')")
        bookstore_database.commit()
        cursor.close()
    


def update_book_by_title(title):
    cursor = bookstore_database.cursor(buffered=True)
    cursor.execute(f"SELECT * FROM books WHERE title LIKE '%{title}%'")
    update_id = input("Please enter the id number of the book that you wish to update (It appears as the first value of your record): ")
    cursor.close()
    updated_title = input("Please enter the new title for this book: ")
    updated_author = input("Please enter the new author for this book: ")
    updated_qty = input("Please enter the new quantity for this book: ")
    cursor = bookstore_database.cursor()
    cursor.execute(f"UPDATE books SET title ='{updated_title}', author ='{updated_author}', qty ='{updated_qty}' WHERE id ='{update_id}'")
    cursor.close()
    bookstore_database.commit()

def search_specific_book(title):

    # Add functionality to adjust for punctuation, case. Add search by author.

    cursor = bookstore_database.cursor()
    cursor.execute(f"SELECT title, author, qty FROM books WHERE title LIKE '%{title}%'")
    search_results = cursor.fetchall()
    cursor.close()
    if len(search_results) > 0:
        return search_results
    else:
        return None

def main():
    menu = ""
    while menu != "0":

        menu = input("""
        Please make a selection from the following options (Please enter 0,1,2,3 or 4):

        1 Enter a book
        2 Update a book
        3 Delete a book
        4 Search for a book
        0 Exit the program
        """)
    
    if menu == "1":
        enter_book()
    
    elif menu == "2":
        title = input("Please enter the title of the book that you wish to update: ")
        update_book_by_title(title)

    elif menu == "3":
        title = input("Please enter the title of the book that you wish to delete: ")
        delete_book_by_title(title)
    
    elif menu == "4":
        title = input("Please enter the title for the book that you wish to search for: ")
        search_specific_book(title)

    elif menu == "0":
        exit()
    
    else:
        print("You have made an invalid selection. Please try again.")

    # Add contingency for program left open or number of sequential invalid selections


bookstore_database.close()