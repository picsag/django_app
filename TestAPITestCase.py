from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class TableAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_table(self):
        url = reverse('table-create')
        data = {
            "title": "My Table",
            "fields": [
                {"name": "name", "type": "string"},
                {"name": "age", "type": "number"},
                {"name": "is_active", "type": "boolean"}
            ]
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "My Table")
        self.assertEqual(len(response.data['fields']), 3)

    def test_update_table(self):
        # Create a table first
        create_url = reverse('table-create')
        create_data = {
            "title": "My Table",
            "fields": [
                {"name": "name", "type": "string"},
                {"name": "age", "type": "number"}
            ]
        }
        create_response = self.client.post(create_url, create_data, format='json')
        table_id = create_response.data['id']

        # Update the table structure
        update_url = reverse('table-update', args=[table_id])
        update_data = {
            "fields": [
                {"name": "email", "type": "string"},
                {"name": "phone", "type": "string"}
            ]
        }

        response = self.client.put(update_url, update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['fields']), 2)
        self.assertTrue('email' in response.data['fields'])
        self.assertTrue('phone' in response.data['fields'])

    def test_add_row_to_table(self):
        # Create a table first
        create_url = reverse('table-create')
        create_data = {
            "title": "My Table",
            "fields": [
                {"name": "name", "type": "string"},
                {"name": "age", "type": "number"}
            ]
        }
        create_response = self.client.post(create_url, create_data, format='json')
        table_id = create_response.data['id']

        # Add a row to the table
        add_row_url = reverse('table-row-create', args=[table_id])
        row_data = {
            "name": "John Doe",
            "age": 30
        }

        response = self.client.post(add_row_url, row_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "John Doe")
        self.assertEqual(response.data['age'], 30)

    def test_get_table_rows(self):
        # Create a table and add rows
        create_url = reverse('table-create')
        create_data = {
            "title": "My Table",
            "fields": [
                {"name": "name", "type": "string"},
                {"name": "age", "type": "number"}
            ]
        }
        create_response = self.client.post(create_url, create_data, format='json')
        table_id = create_response.data['id']

        add_row_url = reverse('table-row-create', args=[table_id])
        row_data = {
            "name": "John Doe",
            "age": 30
        }
        self.client.post(add_row_url, row_data, format='json')

        # Get all rows of the table
        get_rows_url = reverse('table-row-list', args=[table_id])

        response = self.client.get(get_rows_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "John Doe")
        self.assertEqual(response.data[0]['age'], 30)
