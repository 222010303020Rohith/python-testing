import requests  # Import requests library

# API Base URL
BASE_URL = "https://jsonplaceholder.typicode.com/users"

# 📌 1. GET Request - Fetch a User
def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        user = response.json()
        print("\n📌 User Details:")
        print(f"Name: {user['name']}, Email: {user['email']}, City: {user['address']['city']}")
    else:
        print("\n❌ Failed to fetch user. Error:", response.status_code)

# 📌 2. POST Request - Create a New User
def create_user():
    new_user = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "username": "johndoe"
    }
    response = requests.post(BASE_URL, json=new_user)
    if response.status_code == 201:  # 201 means Created Successfully
        user = response.json()
        print("\n✅ User Created Successfully:", user)
    else:
        print("\n❌ Failed to create user. Error:", response.status_code)

# 📌 3. PUT Request - Update an Existing User
def update_user(user_id):
    updated_data = {
        "name": "Updated Name",
        "email": "updated@example.com"
    }
    response = requests.put(f"{BASE_URL}/{user_id}", json=updated_data)
    if response.status_code == 200:
        print("\n✅ User Updated:", response.json())
    else:
        print("\n❌ Failed to update user. Error:", response.status_code)

# 📌 4. DELETE Request - Delete a User
def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print("\n✅ User Deleted Successfully!")
    else:
        print("\n❌ Failed to delete user. Error:", response.status_code)

# Calling Functions for Testing
get_user(1)       # Fetch User with ID 1
create_user()     # Create a New User
update_user(1)    # Update User with ID 1
delete_user(1)    # Delete User with ID