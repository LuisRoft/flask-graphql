# API GraphQL de Inventario

Esta es una API GraphQL construida con Flask para gestionar el inventario de una tienda online. Permite realizar operaciones CRUD sobre productos.

## Requisitos Previos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Docker (opcional)

## Instalación y Ejecución

### Método 1: Usando un Entorno Virtual (venv)

1. Crear y activar el entorno virtual:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```bash
python main.py
```

### Método 2: Usando Docker

1. Construir la imagen:

```bash
docker build -t flask-graphql-store .
```

2. Ejecutar el contenedor:

```bash
docker run -p 5000:5000 flask-graphql-store
```

## Acceso a la API

Una vez en ejecución, puedes acceder a:

- API Homepage: http://localhost:5000
- GraphQL Playground: http://localhost:5000/graphql

## Ejemplos de Queries y Mutations

### Obtener todos los productos

```graphql
query {
  products {
    id
    name
    price
    quantity
    available
    imageUrl
  }
}
```

### Obtener un producto específico

```graphql
query {
  product(id: 1) {
    success
    product {
      id
      name
      price
      quantity
      available
      imageUrl
    }
    message
  }
}
```

### Añadir un nuevo producto

```graphql
mutation {
  addProduct(name: "Nuevo Producto", price: 299.99, quantity: 10, imageUrl) {
    success
    message
    product {
      id
      name
      price
      quantity
      available
      imageUrl
    }
  }
}
```

### Actualizar el stock de un producto

```graphql
mutation {
  updateProductStock(id: 1, quantity: 5) {
    success
    message
    product {
      name
      quantity
      available
    }
  }
}
```

### Eliminar un producto

```graphql
mutation {
  deleteProduct(id: 1) {
    success
    message
  }
}
```

## Pruebas

El proyecto incluye un conjunto completo de pruebas unitarias y de integración que verifican tanto las funciones utilitarias como los endpoints GraphQL.

### Ejecutar las Pruebas

Para ejecutar las pruebas, asegúrate de tener el entorno virtual activado y ejecuta uno de los siguientes comandos:

```bash
python -m unittest test.py
```

o simplemente:

```bash
python test.py
```

### ¿Qué se Prueba?

1. **Funciones Utilitarias**

   - Obtención de todos los productos
   - Obtención de producto por ID
   - Actualización de stock de productos
   - Agregar y eliminar productos

2. **Endpoints GraphQL**
   - Consulta de todos los productos
   - Consulta de producto individual
   - Mutación para actualizar stock

### Notas Importantes

- No es necesario tener el servidor en ejecución para ejecutar las pruebas
- Las pruebas utilizan un cliente de pruebas de Flask (`test_client()`)
- Cada prueba se ejecuta en un entorno aislado gracias a `setUp` y `tearDown`
- Los datos de prueba se restauran después de cada test
