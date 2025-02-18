from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data (acting as a temporary database)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Basic Authentication credentials
USERNAME = 'admin'
PASSWORD = 'password123'


# Basic Authentication function
def check_authentication():
    auth = request.authorization
    if not auth or auth.username != USERNAME or auth.password != PASSWORD:
        return jsonify({"error": "Unauthorized"}), 401
    return None


# 📌 CRUD Operations

# Read all users (GET)
@app.route('/users', methods=['GET'])
def get_users():
    auth_error = check_authentication()
    if auth_error:
        return auth_error
    return jsonify(users)


# Read a single user by ID (GET)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    auth_error = check_authentication()
    if auth_error:
        return auth_error

    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# Create a new user (POST)
@app.route('/users', methods=['POST'])
def create_user():
    auth_error = check_authentication()
    if auth_error:
        return auth_error

    data = request.get_json()  # Get JSON data
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Create new user
    new_user = {"id": len(users) + 1, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201


# Update an existing user (PUT)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    auth_error = check_authentication()
    if auth_error:
        return auth_error

    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(data)  # Update user details
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# Delete a user (DELETE)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    auth_error = check_authentication()
    if auth_error:
        return auth_error

    global users
    users = [u for u in users if u["id"] != user_id]  # Delete user by ID
    return jsonify({"message": "User deleted"}), 200


# Run the Flask app (for development)
if __name__ == '__main__':
    app.run(debug=True)


