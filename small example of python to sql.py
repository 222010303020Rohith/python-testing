import sqlite3

# Connect to SQLite database (Creates the file if it doesn't exist)
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Create a Books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        price REAL
    )
''')
conn.commit()

# Function to insert a book
def insert_book(title, author, price):
    cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (title, author, price))
    conn.commit()
    print(f"✅ Book '{title}' added successfully!")

# Function to read all books
def read_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("\n📚 List of Books:")
    for book in books:
        print(book)

# Function to update book price
def update_price(book_id, new_price):
    cursor.execute("UPDATE books SET price = ? WHERE book_id = ?", (new_price, book_id))
    conn.commit()
    print(f"✅ Book ID {book_id} price updated!")

# Function to delete a book
def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
    conn.commit()
    print(f"❌ Book ID {book_id} deleted!")

# Insert sample books
insert_book("Python Basics", "John Doe", 29.99)
insert_book("Data Science Guide", "Jane Smith", 39.50)
insert_book("AI Revolution", "Elon Tech", 49.99)

# Read books
read_books()

# Update a book price
update_price(1, 34.99)

# Read books after update
read_books()

# Delete a book
delete_book(2)

# Read books after deletion
read_books()

