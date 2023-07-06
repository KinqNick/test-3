```python
# src/views/product_view.py

# Importing necessary libraries
from flask import render_template, request, redirect, url_for

# Importing controllers
from src.controllers.product_controller import get_product, post_product, update_product, delete_product

# Route for product list
@app.route('/products', methods=['GET'])
def product_list():
    products = get_product()
    return render_template('products.html', products=products)

# Route for product detail
@app.route('/products/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    product = get_product(product_id)
    return render_template('product_detail.html', product=product)

# Route for creating a new product
@app.route('/products/new', methods=['POST'])
def new_product():
    product_data = request.form
    post_product(product_data)
    return redirect(url_for('product_list'))

# Route for updating a product
@app.route('/products/<int:product_id>/edit', methods=['POST'])
def edit_product(product_id):
    product_data = request.form
    update_product(product_id, product_data)
    return redirect(url_for('product_detail', product_id=product_id))

# Route for deleting a product
@app.route('/products/<int:product_id>/delete', methods=['POST'])
def delete_product_view(product_id):
    delete_product(product_id)
    return redirect(url_for('product_list'))
```