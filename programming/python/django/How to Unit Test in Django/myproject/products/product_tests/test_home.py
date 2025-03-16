from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product

class ProductAPITestCase(APITestCase):

    def test_get_products(self):
        """Test confirms that the API home page display the text 'Hello, Django!'."""

        # Arrange 
        home_url = reverse('home')
        expected_response = "Hello, Django!"

        # Act
        actual_response = self.client.get(home_url)

        # Assert
        self.assertEqual(actual_response.status_code, status.HTTP_200_OK) # Check the status code to confirm the request was executed successfully 
        self.assertEqual(actual_response.content.decode(), expected_response) # Check the response content to confirm the expected text is displayed
    