from django.db import models
from django.forms import ModelChoiceField
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=2000, null=True, blank=True)
    category = models.CharField(max_length=30, blank=False, null=False, default="other")
    remainder = models.IntegerField(validators=[MinValueValidator(1)])
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name}. {self.description}. {self.category}. {self.remainder}. {self.cost}"


