import sqlite3 

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create 'students' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        department TEXT NOT NULL
    )
''')
connection.commit()

# Function to add a new student
def add_student(name, age, department):
    cursor.execute("INSERT INTO students (name, age, department) VALUES (?, ?, ?)", (name, age, department))
    connection.commit()
    print(f"🎓 Student '{name}' added successfully!")

# Function to display all students
def show_students():
    cursor.execute("SELECT * FROM students")
    student_list = cursor.fetchall()
    
    if student_list:
        print("\n📋 Student Records:")
        for student in student_list:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Department: {student[3]}")
    else:
        print("\n⚠️ No student records found!")

# Function to update a student's age
def update_student_age(student_id, new_age):
    cursor.execute("UPDATE students SET age = ? WHERE student_id = ?", (new_age, student_id))
    connection.commit()
    print(f"✅ Student ID {student_id} age updated to {new_age}!")


# Function to delete a student record
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    connection.commit()
    print(f"❌ Student ID {student_id} removed from records!")

# Adding sample students
add_student("Rahul Sharma", 21, "Computer Science")
add_student("Ananya Verma", 22, "Electrical Engineering")
add_student("Vikram Singh", 20, "Mechanical Engineering")

# Display all students
show_students()

# Update student age
update_student_age(1, 23)

# Show updated records
show_students()

# Delete a student record
delete_student(2)

# Show final records
show_students()


