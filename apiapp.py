import requests  # Import requests library

# API Endpoint
url = "https://jsonplaceholder.typicode.com/users"

# Sending GET request
response = requests.get(url)

# Checking if the request was successful (Status Code 200)
if response.status_code == 200:
    users = response.json()  # Convert JSON response to Python dictionary
    for user in users[:3]:  # Print only the first 3 users
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
else:
    print("Failed to fetch data. Error:", response.status_code)

# Creating a new user (POST Request)
new_user = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "username": "johndoe"
}

response = requests.post(url, json=new_user)

if response.status_code == 201:  # 201 = Created
    print("User Created Successfully:", response.json())
else:
    print("Failed to create user. Error:", response.status_code)

update_url = "https://jsonplaceholder.typicode.com/users/1"

updated_data = {
    "name": "Updated User",
    "email": "updated@example.com"
}

response = requests.put(update_url, json=updated_data)

if response.status_code == 200:
    print("User Updated:", response.json())
else:
    print("Failed to update user. Error:", response.status_code)

delete_url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.delete(delete_url)

if response.status_code == 200:
    print("User Deleted Successfully")
else:
    print("Failed to delete user. Error:", response.status_code)



