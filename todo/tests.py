from django.test import TestCase
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Subtask, Category, Todo
import json


class TestSubtask(TestCase):
    def est_testhomepage(self):
        self.client = Client()
        self.user = Subtask.objects.create(title='test', done='false')

    def test_todo_get(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '/todos/')

# Hier könnte ich noch etwas Hilfe brauchen, danke :D
# Möchtet ihr die backend.js des Join Projekts auch haben?
