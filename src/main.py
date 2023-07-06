import sys
from src.utils import log_error
from src.database import connection
from src.controllers import user_controller, product_controller

def main():
    try:
        # Establish database connection
        db = connection.connect()

        # Initialize controllers
        user_controller.init(db)
        product_controller.init(db)

        # Start the application
        start_app()

    except Exception as e:
        log_error("ERROR_DATABASE_CONNECTION", str(e))
        sys.exit(1)

def start_app():
    while True:
        try:
            # Main application loop
            action = input("Enter action (get/post/update/delete/exit): ")

            if action == "exit":
                break

            entity = input("Enter entity (user/product): ")

            if entity == "user":
                user_controller.handle_action(action)
            elif entity == "product":
                product_controller.handle_action(action)
            else:
                print("Invalid entity. Please enter 'user' or 'product'.")

        except Exception as e:
            log_error("ERROR_INVALID_DATA", str(e))

if __name__ == "__main__":
    main()