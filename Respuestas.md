# Respuestas a preguntas

1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

   - Permite solicitar exactamente los datos necesarios (consultas flexibles)
   - Un único endpoint (/graphql) en lugar de múltiples endpoints REST
   - Sistema de tipos fuerte que ayuda a prevenir errores

2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

   Los tipos se definen en schema.graphql usando SDL (Schema Definition Language), especificando la estructura de datos como Product, Query y Mutation. Los resolvers se implementan en Python (schema.py o algun archivo dedicado al servicio) y manejan la lógica de:

   - Queries: para obtener datos (products, product)
   - Mutations: para modificar datos (updateProductStock, addProduct, deleteProduct)

3. ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

   - Garantiza consistencia de datos desde, esto hara que al recargar la pagina desde el fronted, mantendremos la informacion actualziada
   - Previene manipulaciones maliciosas desde el frontend
   - Mantiene la lógica de negocio centralizada y consistente

4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

   La coherencia se mantiene a través de una mutation específica (updateProductStock) que centraliza toda la lógica de actualización. El resolver se encarga de:

   - Verificar el stock antes y después de cada operación
   - Actualiza automáticamente el estado 'available' a true cuando hay stock (quantity > 0) y false cuando no hay
   - Garantiza que todas las actualizaciones pasen por el mismo flujo de validación
