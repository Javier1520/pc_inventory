# tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Category, Brand, Component

class CategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(slug='category-1', title='Category 1')

    def test_category_list(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Category 1')

    def test_create_category(self):
        data = {'slug': 'category-2', 'title': 'Category 2'}
        response = self.client.post(reverse('categories'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Category 2')

    def test_single_category_retrieve_update_delete(self):
        url = reverse('single_category', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Category 1')

        data = {'slug': 'category-1', 'title': 'Updated Category'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Category')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BrandTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.brand = Brand.objects.create(slug='brand-1', title='Brand 1')

    def test_brand_list_create(self):
        response = self.client.get(reverse('brands'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Brand 1')

        data = {'slug': 'brand-2', 'title': 'Brand 2'}
        response = self.client.post(reverse('brands'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Brand 2')

    def test_single_brand_retrieve_update_delete(self):
        url = reverse('single_brand', kwargs={'slug': self.brand.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Brand 1')

        data = {'slug': 'brand-1', 'title': 'Updated Brand'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Brand')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ComponentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(slug='category-1', title='Category 1')
        self.brand = Brand.objects.create(slug='brand-1', title='Brand 1')
        self.component = Component.objects.create(
            price=100.00, stock=10, name='Component 1', category=self.category, brand=self.brand, user=self.user
        )

    def test_component_list_create(self):
        response = self.client.get(reverse('components'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Component 1')

        data = {
            'price': 200.00,
            'stock': 5,
            'name': 'Component 2',
            'category_id': self.category.id,
            'brand_id': self.brand.id
        }
        response = self.client.post(reverse('components'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Component 2')

    def test_single_component_retrieve_update_delete(self):
        url = reverse('single_component', kwargs={'pk': self.component.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Component 1')

        data = {
            'price': 150.00,
            'stock': 8,
            'name': 'Updated Component',
            'category_id': self.category.id,
            'brand_id': self.brand.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Component')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
