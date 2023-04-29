from rest_framework import serializers

from stock.models import Stock
from product.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
        Product serializer class
    """

    class Meta:
        model = Product
        fields = ['url', 'name', 'quantity', 'price', 'stock', 'image_base64']
        extra_kwargs = {
            'url': {'lookup_field': 'slug',},
            'stock': {'lookup_field': 'slug'},
        }

    def get_fields(self, *args, **kwargs): #Para modificar propiedades dinamicamente
        """        
        """
        fields = super(ProductSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)

        # Así solo permite escoger los stocks del usuari actual.
        if request:
            fields['stock'].queryset = Stock.objects.filter(user=request.user)
        return fields

class StockSerializer(serializers.HyperlinkedModelSerializer):
    """
        Stock serializer class
    """

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ['url', 'name', 'products']
        depth = 1
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

