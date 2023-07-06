```python
from src.database.connection import DatabaseConnection
from src.database.models import User
from src.utils import validate_data, handle_error

class UserController:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get(self, user_id):
        try:
            validate_data(user_id)
            user = self.db_connection.session.query(User).get(user_id)
            if user is None:
                raise ValueError("User not found")
            return user
        except Exception as e:
            handle_error("ERROR_INVALID_DATA", str(e))

    def post(self, user_data):
        try:
            validate_data(user_data)
            new_user = User(**user_data)
            self.db_connection.session.add(new_user)
            self.db_connection.session.commit()
            return "SUCCESS_POST"
        except Exception as e:
            handle_error("ERROR_INVALID_DATA", str(e))

    def update(self, user_id, update_data):
        try:
            validate_data(user_id, update_data)
            user = self.db_connection.session.query(User).get(user_id)
            if user is None:
                raise ValueError("User not found")
            for key, value in update_data.items():
                setattr(user, key, value)
            self.db_connection.session.commit()
            return "SUCCESS_UPDATE"
        except Exception as e:
            handle_error("ERROR_INVALID_DATA", str(e))

    def delete(self, user_id):
        try:
            validate_data(user_id)
            user = self.db_connection.session.query(User).get(user_id)
            if user is None:
                raise ValueError("User not found")
            self.db_connection.session.delete(user)
            self.db_connection.session.commit()
            return "SUCCESS_DELETE"
        except Exception as e:
            handle_error("ERROR_INVALID_DATA", str(e))
```