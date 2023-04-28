import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

IMAGE_SIZE_LIMIT = 1024 * 1024 # 1MB

# Create your models here.
class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name="Nombre")
    slug = models.UUIDField(default = uuid.uuid4, unique=True, verbose_name="Nombre unico de producto")
    quantity = models.IntegerField(default=0, verbose_name="Cantidad", validators=[MinValueValidator(0), MaxValueValidator(9999999999)])
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, verbose_name="Precio", validators=[MinValueValidator(0.0), MaxValueValidator(9999999999)])
    stock = models.ForeignKey('stock.Stock', editable=True, verbose_name='Stock', on_delete=models.CASCADE, related_name="products")
    image_base64 = models.CharField(null=False, blank=False, max_length=IMAGE_SIZE_LIMIT, verbose_name="Imagen Base64")
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def __str__(self):
        return self.name + ' - ' + str(self.pk)
