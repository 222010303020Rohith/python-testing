
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("mydatabase.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")

conn.commit()  # Save changes
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("John Doe", 20, "A"))
dewf
conn.commit()  # Save changes
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()  # Fetch all rows
for row in rows:
    print(row)
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "John Doe"))
conn.commit()
cursor.execute("DELETE FROM students WHERE name = ?", ("John Doe",))
conn.commit()

## this is a new path


