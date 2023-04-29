from drf_yasg.utils import swagger_auto_schema
from .oa_query_parameters import product_get_params

product_list_schema = swagger_auto_schema(
    operation_summary="Obtiene los productos paginadas",
    operation_description='### Ejemplo:\n'+
                          '`GET /products/`',
    tags=['Products - Visualización'],
    manual_parameters=product_get_params
)

product_retrieve_schema = swagger_auto_schema(
    operation_summary="Obtiene un producto por su slug",
    operation_description='### Ejemplo:\n'+
                          '`GET /products/25/`',
    tags=['Products - Visualización']
)

product_create_schema = swagger_auto_schema(
    operation_summary="Crea un producto",
    operation_description='### Ejemplo:\n'+
                          '`POST /products/`',
    tags=['Products - Creación']
)

product_update_schema = swagger_auto_schema(
    operation_summary="Actualiza un producto por su slug",
    operation_description='### Ejemplo:\n'+
                          '`PUT /products/25/`',
    tags=['Products - Actualización']
)

product_partial_update_schema = swagger_auto_schema(
    operation_summary="Actualiza un producto parcialmente por su slug",
    operation_description='### Ejemplo:\n'+
                          '`PATCH /products/25/`',
    tags=['Products - Actualización']
)

product_destroy_schema = swagger_auto_schema(
    operation_summary="Elimina un producto por su slug",
    operation_description='### Ejemplo:\n'+
                          '`DELETE /products/25/`',
    tags=['Products - Eliminación']
)