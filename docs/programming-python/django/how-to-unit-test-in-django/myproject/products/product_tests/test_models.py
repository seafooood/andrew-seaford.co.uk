from django.test import TestCase
from products.models import Product

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name="Laptop", price=1000.00)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1000.00)
