from ariadne import QueryType, MutationType, make_executable_schema, load_schema_from_path

from products import products
from utils import get_all_products, get_product_by_id, update_product_quantity, add_product, delete_product


query = QueryType()
mutation = MutationType()

type_defs = load_schema_from_path("schema.graphql")

@query.field("products")
def resolve_products(_, info):
    return get_all_products()

@query.field("product")
def resolve_product(_, info, id):
    product = get_product_by_id(id)
    return {
        "success": product is not None,
        "product": product,
        "message": "Product with id: " + str(id) + " found" if product else "Product with id: " + str(id) + " not found"
    }


@mutation.field("updateProductStock")
def resolve_update_product_stock(_, info, id, quantity):
    product = update_product_quantity(id, quantity)
    return {
        "product": product,
        "success": product is not None,
        "message": "Product stock updated successfully" if product else "Product with id: " + str(id) + " not found"
    }

@mutation.field("addProduct")
def resolve_add_product(_, info, name, price, quantity):
    new_product = {
        "id": len(products) + 1,
        "name": name,
        "price": price,
        "quantity": quantity,
        "available": quantity > 0
    }

    product = add_product(new_product)

    return {
        "product": product,
        "success": product is not None,
        "message": "Product added successfully" if product else "Failed to add product"
    }

@mutation.field("deleteProduct")
def resolve_delete_product(_, info, id):    
    success = delete_product(id)
    return {
        "success": success,
        "message": "Product deleted successfully" if success else "Product not found"
    }

schema = make_executable_schema(type_defs, query, mutation)