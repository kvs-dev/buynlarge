from django.db import models

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.TextField()

    def __str__(self):
        return f"Order {self.id} - Customer {self.customer.id}"

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Item {self.id} - Order {self.order_id}"

    class Meta:
        db_table = 'order_items' 