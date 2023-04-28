from stock.models import Stock
from product.models import Product
from rest_framework import viewsets, permissions, filters

from .serializers import StockSerializer, ProductSerializer


class StockViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
                       filters.SearchFilter,
                       filters.OrderingFilter,
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
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
                    filters.SearchFilter,
                    filters.OrderingFilter,
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