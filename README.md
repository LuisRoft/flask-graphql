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
