from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id":11, "name": "Alice", "email": "alice@example.com"},
    {"id":22, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = next((u for u in users if u['id'] == id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/user/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    user = next((u for u in users if u['id'] == id), None)
    if user:
        update_data = request.get_json()
        user.update(update_data)
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    global users
    before_count = len(users)
    users = [u for u in users if u['id'] != id]
    if len(users) < before_count:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/')
def home():
    return "Flask User API is running!"

if __name__ == "__main__":
    app.run(debug=True)
