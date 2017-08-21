from django.test import TestCase
from django.test.client import Client

from .models import Todo


class TodoTests(TestCase):

    def setUp(self):
        """Lets create one todo that we can use within the tests below"""
        self.example_todo = Todo.objects.create(description="test")

    def test_model_fields_exist(self):
        self.assertTrue(Todo._meta.get_field('user'))
        self.assertTrue(Todo._meta.get_field('description'))
        self.assertTrue(Todo._meta.get_field('due_date'))

    def test_index_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_todo_list_view(self):
        c = Client()
        response = c.get('/todos/')
        self.assertEqual(response.status_code, 200)

    def test_todo_detail_view(self):
        c = Client()
        response = c.get('/todo/1/')
        self.assertEqual(response.status_code, 200)

    def test_todo_create_view(self):
        c = Client()
        data = {'description': 'new'}
        response = c.post('/todo/create/', data)
        self.assertEqual(response.status_code, 302) # test redirection
        self.assertEqual(response.url, '/todo/2/')

    def test_todo_update_view(self):
        c = Client()
        data = {'description': 'changed'}
        response = c.post('/todo/1/update/', data)
        self.assertEqual(response.status_code, 302) # test redirection
        self.assertEqual(response.url, '/todo/1/')

    def test_todo_delete_view(self):
        c = Client()
        response = c.post('/todo/1/delete/')
        self.assertEqual(response.status_code, 302) # test redirection
        self.assertEqual(Todo.objects.all().count(), 0)
