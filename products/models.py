from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
