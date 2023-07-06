```python
from src.database.connection import DatabaseConnection
from src.database.models import Product
from src.utils import handle_error, validate_data

class ProductController:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    @handle_error
    @validate_data
    def get(self, product_id):
        product = self.db_connection.session.query(Product).get(product_id)
        if product is None:
            raise Exception("ERROR_INVALID_DATA")
        return product

    @handle_error
    @validate_data
    def post(self, product_data):
        new_product = Product(**product_data)
        self.db_connection.session.add(new_product)
        self.db_connection.session.commit()
        return "SUCCESS_POST"

    @handle_error
    @validate_data
    def update(self, product_id, product_data):
        product = self.db_connection.session.query(Product).get(product_id)
        if product is None:
            raise Exception("ERROR_INVALID_DATA")
        for key, value in product_data.items():
            setattr(product, key, value)
        self.db_connection.session.commit()
        return "SUCCESS_UPDATE"

    @handle_error
    def delete(self, product_id):
        product = self.db_connection.session.query(Product).get(product_id)
        if product is None:
            raise Exception("ERROR_INVALID_DATA")
        self.db_connection.session.delete(product)
        self.db_connection.session.commit()
        return "SUCCESS_DELETE"
```