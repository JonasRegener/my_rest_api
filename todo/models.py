from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date, timedelta

class Todo(models.Model):
    TODO_CATEGORY_CHOICES = [
    ('M', 'Media'),
    ('D', 'Design'),
    ('MA', 'Marketing'),
    ('B', 'Backoffice'),
    ('S', 'Sales'),
    ('-', 'None')
]
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    due_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    category = models.CharField(max_length=10,choices=TODO_CATEGORY_CHOICES, default='None')
    # due_date = models.DateField(default=datetime.timedelta(days=1))
 #   def time_passed(self):
 #       today = date.today()
 #       dif = today - self.created_at
 #       return dif.days

""" 
class User(models.Model):
    email = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

     """