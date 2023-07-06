```python
# Importing necessary libraries
from flask import render_template, request, redirect, url_for
from src.controllers.user_controller import get_user, post_user, update_user, delete_user

# Defining the id names of DOM elements
user_list_id = "user-list"
user_detail_id = "user-detail"

# Route for displaying the user list
@app.route('/users', methods=['GET'])
def user_list():
    users = get_user()
    return render_template('users.html', users=users, user_list_id=user_list_id)

# Route for displaying a specific user detail
@app.route('/users/<int:user_id>', methods=['GET'])
def user_detail(user_id):
    user = get_user(user_id)
    return render_template('user_detail.html', user=user, user_detail_id=user_detail_id)

# Route for creating a new user
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.form
    post_user(user_data)
    return redirect(url_for('user_list'))

# Route for updating an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_detail(user_id):
    user_data = request.form
    update_user(user_id, user_data)
    return redirect(url_for('user_detail', user_id=user_id))

# Route for deleting a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_detail(user_id):
    delete_user(user_id)
    return redirect(url_for('user_list'))
```