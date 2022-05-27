from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Product
from django.contrib.auth.models import User


class TestProductView(TestCase):
    def setUp(self):
        self.test_product = Product.objects.create(
            title="test_products",
            description="Testing products",
            image_link="https://unsplash.com/photos/pA2v_MZHHro",
            published=True,
            user=User.objects.create_user(
                'john', 'lennon@thebeatles.com', 'johnpassword')
        )

    def test_authentication_required(self):
        self.client.login(username='john', password='johnpassword')
        url = reverse('products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_products_model(self):
        product = Product.objects.get(id=1)
        actual_title = product.title
        self.assertEqual(actual_title, self.test_product.title)
