from drf_yasg.utils import swagger_auto_schema
from .oa_query_parameters import stock_get_params

stock_list_schema = swagger_auto_schema(
    operation_summary="Obtiene los stocks",
    operation_description='### Ejemplo:\n'+
                          '`GET /stocks/`',
    tags=['Stocks - Visualización'],
    manual_parameters=stock_get_params
)

stock_retrieve_schema = swagger_auto_schema(
    operation_summary="Obtiene un stock por su slug",
    operation_description='### Ejemplo:\n'+
                          '`GET /stocks/c1396015-6d8b-4215-9096-9bd9136072d9/`',
    tags=['Stocks - Visualización'],
)

stock_create_schema = swagger_auto_schema(
    operation_summary="Crea un stock",
    operation_description='### Ejemplo:\n'+
                          '`POST /stocks/`',
    tags=['Stocks - Creación']
)

stock_update_schema = swagger_auto_schema(
    operation_summary="Actualiza un stock por su slug",
    operation_description='### Ejemplo:\n'+
                          '`PUT /stocks/c1396015-6d8b-4215-9096-9bd9136072d9/`',
    tags=['Stocks - Actualización']
)

stock_partial_update_schema = swagger_auto_schema(
    operation_summary="Actualiza un stock parcialmente por su slug",
    operation_description='### Ejemplo:\n'+
                          '`PATCH /stocks/c1396015-6d8b-4215-9096-9bd9136072d9/`',
    tags=['Stocks - Actualización']
)

stock_destroy_schema = swagger_auto_schema(
    operation_summary="Elimina un stock por su slug",
    operation_description='### Ejemplo:\n'+
                          '`DELETE /stocks/c1396015-6d8b-4215-9096-9bd9136072d9/`',
    tags=['Stocks - Eliminación']
)