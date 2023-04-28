import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name="Nombre")
    slug = models.UUIDField(default = uuid.uuid4, unique=True, verbose_name="Nombre unico de stock")
    user = models.ForeignKey(User, editable=True, verbose_name='Usuario', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        ordering = ['name']

    def __str__(self):
        return self.name + '-' + str(self.pk)
