from django.core.management.base import BaseCommand
from django.utils import timezone
from products.models import Product
from customers.models import Customer
from orders.models import Order, OrderItem
from stock.models import Stock
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Create Products
        products_data = [
            {'name': 'Laptop Pro X', 'description': 'High-end laptop with 16GB RAM', 'price': '1299.99', 'category': 'Electronics'},
            {'name': 'Smartphone Y20', 'description': 'Latest smartphone model', 'price': '799.99', 'category': 'Electronics'},
            {'name': 'Coffee Maker Deluxe', 'description': 'Automatic coffee maker with timer', 'price': '89.99', 'category': 'Appliances'},
            {'name': 'Running Shoes Air', 'description': 'Professional running shoes', 'price': '129.99', 'category': 'Sports'},
            {'name': 'Gaming Mouse RGB', 'description': 'RGB gaming mouse with 6 buttons', 'price': '59.99', 'category': 'Gaming'},
            {'name': 'Wireless Earbuds', 'description': 'Bluetooth 5.0 wireless earbuds', 'price': '149.99', 'category': 'Electronics'},
            {'name': 'Smart Watch Pro', 'description': 'Fitness tracking smartwatch', 'price': '199.99', 'category': 'Electronics'},
            {'name': 'Backpack XL', 'description': 'Large capacity hiking backpack', 'price': '79.99', 'category': 'Outdoor'},
            {'name': 'Desk Lamp LED', 'description': 'Adjustable LED desk lamp', 'price': '39.99', 'category': 'Home'},
            {'name': 'Keyboard Mechanical', 'description': 'RGB mechanical keyboard', 'price': '129.99', 'category': 'Gaming'}
        ]

        for data in products_data:
            Product.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Products created successfully'))

        # Create Customers
        customers_data = [
            {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@email.com', 'phone': '123-456-7890'},
            {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane.smith@email.com', 'phone': '234-567-8901'},
            {'first_name': 'Robert', 'last_name': 'Johnson', 'email': 'robert.j@email.com', 'phone': '345-678-9012'},
            {'first_name': 'Maria', 'last_name': 'Garcia', 'email': 'maria.g@email.com', 'phone': '456-789-0123'},
            {'first_name': 'David', 'last_name': 'Brown', 'email': 'david.b@email.com', 'phone': '567-890-1234'},
            {'first_name': 'Lisa', 'last_name': 'Wilson', 'email': 'lisa.w@email.com', 'phone': '678-901-2345'},
            {'first_name': 'Michael', 'last_name': 'Taylor', 'email': 'michael.t@email.com', 'phone': '789-012-3456'},
            {'first_name': 'Sarah', 'last_name': 'Anderson', 'email': 'sarah.a@email.com', 'phone': '890-123-4567'},
            {'first_name': 'James', 'last_name': 'Martinez', 'email': 'james.m@email.com', 'phone': '901-234-5678'},
            {'first_name': 'Emma', 'last_name': 'Thomas', 'email': 'emma.t@email.com', 'phone': '012-345-6789'}
        ]

        for data in customers_data:
            Customer.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Customers created successfully'))

        # Create Orders
        orders = []
        statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']
        customers = list(Customer.objects.all())

        for _ in range(10):
            order = Order.objects.create(
                customer_id=random.choice(customers).id,
                order_date=timezone.now(),
                status=random.choice(statuses)
            )
            orders.append(order)
        self.stdout.write(self.style.SUCCESS('Orders created successfully'))

        # Create Order Items
        products = list(Product.objects.all())
        for order in orders:
            # Create 1-3 items per order
            for _ in range(random.randint(1, 3)):
                product = random.choice(products)
                OrderItem.objects.create(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=random.randint(1, 5),
                    price=product.price
                )
        self.stdout.write(self.style.SUCCESS('Order Items created successfully'))

        # Create Stock
        for product in products:
            Stock.objects.create(
                product_id=product.id,
                quantity=random.randint(10, 100)
            )
        self.stdout.write(self.style.SUCCESS('Stock created successfully'))

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!')) 