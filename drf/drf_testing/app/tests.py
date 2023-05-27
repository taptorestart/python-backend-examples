
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Category


class CategoryTests(APITestCase):

    VIEWNAME_LIST = 'category-list'
    VIEWNAME_DETAIL = 'category-detail'

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='password', is_staff=True)

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Tea')

    def test_create_category_anonymous_403(self):
        url = reverse(self.VIEWNAME_LIST)
        data = {'name': 'Coffee'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_category_staff_201(self):
        url = reverse(self.VIEWNAME_LIST)
        data = {'name': 'Coffee'}
        self.client.force_login(user=self.user)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_anonymous_403(self):
        url = reverse(self.VIEWNAME_LIST)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_staff_200(self):
        url = reverse(self.VIEWNAME_LIST)
        self.client.force_login(user=self.user)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Tea')

    def test_retrieve_anonymous_403(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_staff_200(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        self.client.force_login(user=self.user)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Coffee')

    def test_update_anonymous_403(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        data = {'name': 'Dessert'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_staff_200(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        data = {'name': 'Dessert'}
        self.client.force_login(user=self.user)
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Dessert')

    def test_partial_update_anonymous_403(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        data = {'name': 'Dessert'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_staff_200(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        data = {'name': 'Dessert'}
        self.client.force_login(user=self.user)
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Dessert')

    def test_destroy_anonymous_403(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        data = {'name': 'Dessert'}
        response = self.client.delete(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_staff_200(self):
        category = Category.objects.create(name='Coffee')

        url = reverse(self.VIEWNAME_DETAIL, args=[category.id])
        data = {'name': 'Dessert'}
        self.client.force_login(user=self.user)
        response = self.client.delete(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
