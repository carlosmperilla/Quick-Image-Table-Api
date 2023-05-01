from django.db import models
from django.core.validators import MaxValueValidator

LIMIT_SIZE_KB = 1024 * 100 # 100 MB in KB By PythonAnyWhere

# Create your models here.
class Spacelimiter(models.Model):
    size = models.FloatField(default=0.0, validators=[MaxValueValidator(LIMIT_SIZE_KB)]) # Limite en KB
