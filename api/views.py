from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.views.decorators.cache import cache_control

from stock.models import Stock
from product.models import Product

from rest_framework import viewsets, permissions, filters

from .serializers import StockSerializer, ProductSerializer

from .custom_permissions import SpaceLimiterPermission

from .handle_custom_filters.custom_filters import (
                                ByStockAttrFilterBackend,
                                ByProductAttrFilterBackend,
                                ByQuantityRangeFilterBackend,
                                ByPriceRangeFilterBackend,
                            )
from .custom_schemas.stock_schemas import (
                            stock_list_schema,
                            stock_retrieve_schema,
                            stock_create_schema,
                            stock_update_schema,
                            stock_partial_update_schema,
                            stock_destroy_schema
                         )
from .custom_schemas.product_schemas import (
                            product_list_schema,
                            product_retrieve_schema,
                            product_create_schema,
                            product_update_schema,
                            product_partial_update_schema,
                            product_destroy_schema
                         )


@method_decorator(name='list', decorator=stock_list_schema)
@method_decorator(name='retrieve', decorator=stock_retrieve_schema)
@method_decorator(name='create', decorator=stock_create_schema)
@method_decorator(name='update', decorator=stock_update_schema)
@method_decorator(name='partial_update', decorator=stock_partial_update_schema)
@method_decorator(name='destroy', decorator=stock_destroy_schema)
@method_decorator(name='list', decorator=cache_control(must_revalidate=True))
class StockViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver, crear, modificar y eliminar Stocks** para el *usuario actual*.
    ## <span style="color:darkslateblue">Filtros</span>
    Puede usar get-parameters para **filtrar por atributo**, por ejemplo.
    > api/stocks/?name=stockname
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated, SpaceLimiterPermission]
    filter_backends = [
                       filters.SearchFilter,
                       filters.OrderingFilter,
                       ByStockAttrFilterBackend,
                       ]
    search_fields = ['name', 'slug']
    ordering_fields = ['name', 'slug']
    ordering = ['name', 'slug']
    lookup_field = 'slug'

    def initial(self, request, *args, **kwargs):
        self.cache_key = f"stocks_cache_{self.request.user.pk}"
        return super().initial(request, *args, **kwargs)

    def get_queryset(self):
        """
            Gets Queryset and assigns current user' primary key
        """

        cache_queryset = cache.get(self.cache_key)
        if cache_queryset is None:
            cache_queryset = self.queryset.filter(user__pk = self.request.user.pk)
            cache.set(self.cache_key, cache_queryset, 60*60*2) # expires in 2h at the latest
        return cache_queryset

    def perform_create(self, serializer):
        """
            We override the creation to assign the user to it.
        """
        cache.delete(self.cache_key)
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
            We override the update to assign the user to it.
        """
        cache.delete(self.cache_key)
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        cache.delete(self.cache_key)
        return super().perform_destroy(instance)
        

@method_decorator(name='list', decorator=product_list_schema)
@method_decorator(name='retrieve', decorator=product_retrieve_schema)
@method_decorator(name='create', decorator=product_create_schema)
@method_decorator(name='update', decorator=product_update_schema)
@method_decorator(name='partial_update', decorator=product_partial_update_schema)
@method_decorator(name='destroy', decorator=product_destroy_schema)
@method_decorator(name='list', decorator=cache_control(must_revalidate=True))
class ProductViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver, crear, modificar y eliminar Productos** para el *usuario actual*.
    ## <span style="color:darkslateblue">Filtros</span>
    
    Puede usar get-parameters para **filtrar por atributo**, por ejemplo.
    
    > api/cards/?name=productname
    
    Tambien por **rango**, con *min_quantity* y *max_quantity* o con *min_price* y *max_price*.
    > api/cards/?min_quantity=12&max_quantity=80
    
    > api/cards/?min_price=50.2
    
    > api/cards/?max_price=700.45
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, SpaceLimiterPermission]
    filter_backends = [
                    filters.SearchFilter,
                    filters.OrderingFilter,
                    ByProductAttrFilterBackend,
                    ByQuantityRangeFilterBackend,
                    ByPriceRangeFilterBackend,
    ]
    search_fields = ['name', 'slug']
    ordering_fields = ['name', 'slug', 'quantity', 'price']
    ordering = ['name', 'slug']
    lookup_field = 'slug'

    def initial(self, request, *args, **kwargs):
        self.cache_key = f"products_cache_{self.request.user.pk}"
        self.cache_keys = [f"products_cache_{self.request.user.pk}", f"stocks_cache_{self.request.user.pk}"]
        return super().initial(request, *args, **kwargs)

    def get_queryset(self):
        """
            Gets Queryset and assigns current user' primary key
        """

        cache_queryset = cache.get(self.cache_key)
        if cache_queryset is None:
            cache_queryset = self.queryset.filter(stock__user__pk = self.request.user.pk)
            cache.set(self.cache_key, cache_queryset, 60*60*2)  # expires in 2h at the latest
        
        return cache_queryset
   
    def perform_create(self, serializer):
        cache.delete_many(self.cache_keys)
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        cache.delete_many(self.cache_keys)
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        cache.delete_many(self.cache_keys)
        return super().perform_destroy(instance)