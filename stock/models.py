from django.db import models

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Stock for product {self.product.id}: {self.quantity}"

    class Meta:
        db_table = 'stock' 