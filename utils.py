from products import products

def get_all_products():
    return products

def get_product_by_id(id):
    for product in products:
        if product['id'] == id:
            return product
    return None

def update_product_quantity(id, quantity):
    product = get_product_by_id(id)
    if product:
        new_stock = max(0, product["quantity"] + quantity)
        product["quantity"] = new_stock

        product["available"] = new_stock > 0

        return product
    return None

def add_product(product):
    products.append(product)
    return product

def delete_product(id):
    product = get_product_by_id(id)
    if product:
        products.remove(product)
        return True
    return False

def get_product_by_name(name):
    for product in products:
        if product['name'] == name:
            return product
    return None


