from mongoengine import Document, StringField, IntField, BooleanField, connect

# ✅ Connect to MongoDB
connect('student_db', host='localhost', port=27017)

# ✅ Define the Student Model
class Student(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    branch = StringField(required=True)
    course = StringField(required=True)
    mode = StringField(choices=["online", "offline"])
    paid = BooleanField(default=False)
    amount = IntField()

# 1️⃣ CREATE: Insert Student Records
def create_students():
    student1 = Student(name="Sai", age=20, branch="CSE", course="Python", mode="online", paid=True, amount=1499)
    student2 = Student(name="Rohith", age=21, branch="CSE", course="SQL", mode="online", paid=True, amount=1499)
    
    student1.save()
    student2.save()
    print("✅ Students Inserted Successfully!\n")

# 2️⃣ READ: Get All Students
def get_all_students():
    students = Student.objects()
    print("📌 List of Students:")
    for student in students:
        print(student.to_json())

# 3️⃣ READ: Get a Single Student by Name
def get_student_by_name(name):
    student = Student.objects(name=name).first()
    print(f"\n📌 Student Details for '{name}':")
    print(student.to_json() if student else "❌ Student Not Found")

# 4️⃣ UPDATE: Update a Student's Age
def update_student_age(name, new_age):
    student = Student.objects(name=name).first()
    if student:
        student.update(set__age=new_age)
        print(f"\n✅ Updated {name}'s age to {new_age}")
    else:
        print("❌ Student Not Found")

# 5️⃣ DELETE: Remove a Student
def delete_student(name):
    student = Student.objects(name=name).first()
    if student:
        student.delete()
        print(f"\n✅ Deleted '{name}' from the database")
    else:
        print("❌ Student Not Found")

# ✅ Run CRUD Functions
if __name__ == "__main__":
    create_students()               # Insert Data 
    get_all_students()              # Read All Data
    get_student_by_name("Sai")      # Read One Student
    update_student_age("Rohith", 22) # Update Age
    delete_student("Sai")           # Delete Student
 