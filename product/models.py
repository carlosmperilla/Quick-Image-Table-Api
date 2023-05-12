import uuid
import sys

from django.db import models
from django.db.models import F
from django.db.models.signals import pre_save, pre_delete
from django.core.validators import MinValueValidator, MaxValueValidator

from api.models import Spacelimiter

IMAGE_SIZE_LIMIT = 1024 * 1024 # 1MB

# Create your models here.
class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name="Nombre")
    slug = models.UUIDField(default = uuid.uuid4, unique=True, verbose_name="Nombre unico de producto")
    quantity = models.IntegerField(default=0, verbose_name="Cantidad", validators=[MinValueValidator(0), MaxValueValidator(9999999999)])
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, verbose_name="Precio", validators=[MinValueValidator(0.0), MaxValueValidator(9999999999)])
    stock = models.ForeignKey('stock.Stock', editable=True, verbose_name='Stock', on_delete=models.CASCADE, related_name="products")
    image_base64 = models.TextField(null=False, blank=False, max_length=IMAGE_SIZE_LIMIT, verbose_name="Imagen Base64")
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def __str__(self):
        return self.name + ' - ' + str(self.pk)

def add_size_tracker(sender, instance, *args, **kwargs):
    """
        Add size of Spacelimiter
    """

    product_img_size = sys.getsizeof(instance.image_base64) / 1024 # KB
    
    if not Spacelimiter.objects.exists():
        Spacelimiter.objects.create(size=product_img_size)
    else:
        Spacelimiter.objects.update(size=F("size") + product_img_size)


def sub_size_tracker(sender, instance, *args, **kwargs):
    """
        Substract size of Spacelimiter
    """

    product_img_size = sys.getsizeof(instance.image_base64) / 1024 # KB
    
    Spacelimiter.objects.update(size=F("size") - product_img_size)


pre_save.connect(add_size_tracker, sender=Product)
pre_delete.connect(sub_size_tracker, sender=Product)
