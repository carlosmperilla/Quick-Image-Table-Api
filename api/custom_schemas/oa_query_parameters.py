from drf_yasg import openapi

search_param = openapi.Parameter('search', openapi.IN_QUERY, description="Un término de búsqueda", type=openapi.TYPE_STRING)
page_param = openapi.Parameter('page', openapi.IN_QUERY, description="Un número de página dentro del conjunto de resultados paginado.", type=openapi.TYPE_INTEGER)

stock_ordering_param = openapi.Parameter('ordering', openapi.IN_QUERY, 
                                        description="Qué campo utilizar al ordenar los resultados",
                                        type=openapi.TYPE_STRING, 
                                        enum=[
                                                'name',
                                                '-name',
                                                'slug',
                                                '-slug'
                                                ])

stock_name_param = openapi.Parameter('name', openapi.IN_QUERY, description="Nombre", type=openapi.TYPE_STRING)

product_ordering_param = openapi.Parameter('ordering', openapi.IN_QUERY, 
                                        description="Qué campo utilizar al ordenar los resultados",
                                        type=openapi.TYPE_STRING, 
                                        enum=[
                                                'name',
                                                '-name',
                                                'slug',
                                                '-slug'
                                                'quantity',
                                                '-quantity',
                                                'price',
                                                '-price',
                                                ])

product_name_param = openapi.Parameter('name', openapi.IN_QUERY, description="Nombre", type=openapi.TYPE_STRING)
product_quantity_param = openapi.Parameter('quantity', openapi.IN_QUERY, description="Cantidad", type=openapi.TYPE_INTEGER)
product_minquantity_param = openapi.Parameter('min_quantity', openapi.IN_QUERY, description="Mínima cantidad", type=openapi.TYPE_INTEGER)
product_maxquantity_param = openapi.Parameter('max_quantity', openapi.IN_QUERY, description="Máxima cantidad", type=openapi.TYPE_INTEGER)
product_price_param = openapi.Parameter('price', openapi.IN_QUERY, description="Precio", type=openapi.TYPE_NUMBER)
product_minprice_param = openapi.Parameter('min_price', openapi.IN_QUERY, description="Mínimo precio", type=openapi.TYPE_NUMBER)
product_maxprice_param = openapi.Parameter('max_price', openapi.IN_QUERY, description="Máxima precio", type=openapi.TYPE_NUMBER)

stock_get_params = [
                    stock_name_param,
                    search_param,
                    page_param,
                        ]

product_get_params = [
                    product_ordering_param,
                    product_name_param,
                    product_quantity_param,
                    product_minquantity_param,
                    product_maxquantity_param,
                    product_price_param,
                    product_minprice_param,
                    product_maxprice_param,
                    search_param,
                    page_param,
                        ]