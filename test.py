import unittest
from main import app
from utils import (
    get_all_products, 
    get_product_by_id, 
    update_product_quantity,
    add_product,
    delete_product
)
from products import products

class TestUtilsFunctions(unittest.TestCase):
    def setUp(self):
        # Guardar una copia profunda de los productos originales
        self.original_products = []
        for product in products:
            self.original_products.append(product.copy())
        
    def tearDown(self):
        # Restaurar los productos originales después de cada prueba
        products.clear()
        for product in self.original_products:
            products.append(product.copy())

    def test_get_all_products(self):
        result = get_all_products()
        self.assertEqual(len(result), len(self.original_products))
        self.assertEqual(result[0]['name'], "iPhone 14 Pro")

    def test_get_product_by_id(self):
        product = get_product_by_id(1)
        self.assertIsNotNone(product)
        self.assertEqual(product['name'], "iPhone 14 Pro")
        
        # Probar producto que no existe
        product = get_product_by_id(999)
        self.assertIsNone(product)

    def test_update_product_quantity(self):
        # Verificar cantidad inicial
        initial_product = get_product_by_id(1)
        self.assertEqual(initial_product['quantity'], 15, "La cantidad inicial debe ser 15")

        # Aumentar cantidad
        product = update_product_quantity(1, 5)
        self.assertEqual(product['quantity'], 20, "La cantidad después de añadir 5 debe ser 20")  # 15 + 5
        self.assertTrue(product['available'])

        # Verificar que el cambio persistió
        updated_product = get_product_by_id(1)
        self.assertEqual(updated_product['quantity'], 20, "La cantidad debe mantenerse en 20")

        # Reducir cantidad a 0
        product = update_product_quantity(1, -20)
        self.assertEqual(product['quantity'], 0, "La cantidad después de restar 20 debe ser 0")
        self.assertFalse(product['available'])

        # Verificar que el cambio a 0 persistió
        final_product = get_product_by_id(1)
        self.assertEqual(final_product['quantity'], 0, "La cantidad final debe ser 0")

    def test_add_and_delete_product(self):
        new_product = {
            "id": 7,
            "name": "Test Product",
            "price": 99.99,
            "quantity": 10,
            "available": True,
            "imageUrl": "test.jpg"
        }
        
        # Probar añadir
        added_product = add_product(new_product)
        self.assertEqual(added_product['name'], "Test Product")
        self.assertEqual(len(products), len(self.original_products) + 1)

        # Probar eliminar
        result = delete_product(7)
        self.assertTrue(result)
        self.assertEqual(len(products), len(self.original_products))

class TestGraphQLEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.graphql_url = '/graphql'
        # Guardar una copia profunda de los productos originales
        self.original_products = []
        for product in products:
            self.original_products.append(product.copy())
        
    def tearDown(self):
        # Restaurar los productos originales después de cada prueba
        products.clear()
        for product in self.original_products:
            products.append(product.copy())

    def test_get_all_products_query(self):
        query = """
        query {
            products {
                id
                name
                price
            }
        }
        """
        response = self.app.post(
            self.graphql_url,
            json={'query': query}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('data', data)
        self.assertIn('products', data['data'])
        self.assertGreater(len(data['data']['products']), 0)

    def test_get_single_product_query(self):
        query = """
        query {
            product(id: 1) {
                success
                product {
                    name
                    price
                }
                message
            }
        }
        """
        response = self.app.post(
            self.graphql_url,
            json={'query': query}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('data', data)
        self.assertTrue(data['data']['product']['success'])

    def test_update_product_stock_mutation(self):
        mutation = """
        mutation {
            updateProductStock(id: 1, quantity: 5) {
                success
                product {
                    quantity
                    available
                }
                message
            }
        }
        """
        response = self.app.post(
            self.graphql_url,
            json={'query': mutation}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('data', data)
        self.assertTrue(data['data']['updateProductStock']['success'])

if __name__ == '__main__':
    unittest.main() 