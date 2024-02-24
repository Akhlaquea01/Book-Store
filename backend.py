import sqlite3

# Function to connect to the database and create a 'book' table if it doesn't exist
def connect():
    conn = sqlite3.connect("books.db")  # Connect to or create the database file 'books.db'
    cur = conn.cursor()  # Create a cursor object to interact with the database
    # Create the 'book' table if it doesn't already exist, with columns: id, title, author, year, isbn
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection to the database

# Function to insert a new book into the database
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    # Insert a new row into the 'book' table with the provided title, author, year, and isbn
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection to the database
    view()  # Call view() function to display all books after insertion

# Function to view all books in the database
def view():
    conn = sqlite3.connect("books.db")  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute("SELECT * FROM book")  # Execute a select query to fetch all rows from the 'book' table
    rows = cur.fetchall()  # Fetch all rows returned by the query
    conn.close()  # Close the connection to the database
    return rows  # Return the fetched rows

# Function to search for books based on title, author, year, or isbn
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    # Execute a select query with optional search parameters
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()  # Fetch all rows returned by the query
    conn.close()  # Close the connection to the database
    return rows  # Return the fetched rows

# Function to delete a book from the database based on its id
def delete(id):
    conn = sqlite3.connect("books.db")  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute("DELETE FROM book WHERE id=?", (id,))  # Delete the book with the specified id
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection to the database

# Function to update the details of a book in the database
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    # Update the title, author, year, and isbn of the book with the specified id
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection to the database

# Call the connect() function to ensure the 'book' table exists
connect()

# Example usage of the functions:
# insert("The Sun", "John Smith", 1918, 913123132)  # Insert a new book
# delete(3)  # Delete a book with id=3
# update(4, "The moon", "John Smooth", 1917, 99999)  # Update details of a book with id=4
# print(view())  # View all books in the database
# print(search(author="John Smooth"))  # Search for books by author
