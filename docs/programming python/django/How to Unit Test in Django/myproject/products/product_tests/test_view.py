from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product

class ProductAPITestCase(APITestCase):

    def setUp(self):
        """Setup test data: Create a sample product."""
        self.product = Product.objects.create(name="Laptop", price=1000.00)
        self.list_url = reverse('product-list')  # DRF router auto-generates names
        self.detail_url = reverse('product-detail', kwargs={'pk': self.product.id})

    def test_get_products(self):
        """Test confirms that the API returns a list of all products."""

        # Arrange - No additional setup needed

        # Act
        response = self.client.get(self.list_url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Check the status code to confirm the request was executed successfully 
    
    def test_create_product(self):
        """Test confirms that a new product can be created via API."""

        # Arrange
        data = {"name": "Phone", "price": 500.00}

        # Act
        response = self.client.post(self.list_url, data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
    
    def test_get_product_detail(self):
        """Test confirms that an individual product's details can be retrieved."""

        # Arrange - Product is already created in setUp()

        # Act
        response = self.client.get(self.detail_url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Check the status code to confirm a record was created
        self.assertEqual(response.data['name'], "Laptop") # Confirm the products list contains to items
    
    def test_update_product(self):
        """Test confirms that an existing product can be updated."""

        # Arrange
        data = {"name": "Smartphone", "price": 600.00}

        # Act
        response = self.client.put(self.detail_url, data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Smartphone") # Confirm name change
        self.assertEqual(self.product.price, 600.00) # Confirm price change

    def test_delete_product(self):
        """Test confirms that a product can be deleted via API."""

        # Arrange - Product exists (created by setup)

        # Act
        response = self.client.delete(self.detail_url)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) # Confirm deletion
        self.assertEqual(Product.objects.count(), 0) # Confirm product count is 0