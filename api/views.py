from stock.models import Stock
from product.models import Product
from rest_framework import viewsets, permissions, filters

from .serializers import StockSerializer, ProductSerializer
from .handle_custom_filters.custom_filters import (
                                ByStockAttrFilterBackend,
                                ByProductAttrFilterBackend,
                                ByQuantityRangeFilterBackend,
                                ByPriceRangeFilterBackend,
                            )


class StockViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver, crear, modificar y eliminar Stocks** para el *usuario actual*.
    ## <span style="color:darkslateblue">Filtros</span>
    Puede usar get-parameters para **filtrar por atributo**, por ejemplo.
    > api/stocks/?name=stockname
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
                       filters.SearchFilter,
                       filters.OrderingFilter,
                       ByStockAttrFilterBackend,
                       ]
    search_fields = ['name', 'slug']
    ordering_fields = ['name', 'slug']
    ordering = ['name', 'slug']
    lookup_field = 'slug'

    def get_queryset(self):
        """
            Gets Queryset and assigns current user' primary key
        """
        return self.queryset.filter(user__pk = self.request.user.pk)

    def perform_create(self, serializer):
        """
            We override the creation to assign the user to it.
        """
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
            We override the update to assign the user to it.
        """
        serializer.save(user=self.request.user)



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
    permission_classes = [permissions.IsAuthenticated]
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

    def get_queryset(self):
        """
            Gets Queryset and assigns current user' primary key
        """
        return self.queryset.filter(stock__user__pk = self.request.user.pk)