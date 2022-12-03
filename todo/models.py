from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date, timedelta


    

class Subtask(models.Model):
    title = models.CharField(max_length=30)


class Todo(models.Model):
    TODO_CATEGORY_CHOICES = [
    ('M', 'Media'),
    ('D', 'Design'),
    ('MA', 'Marketing'),
    ('B', 'Backoffice'),
    ('S', 'Sales'),
    ('-', 'None')
]
    PRIO_CATEGORY_CHOICES = [
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low')
]
    STATUS_CATEGORY_CHOICES = [
    ('1', 'To do'),
    ('2', 'In progress'),
    ('3', 'Awaiting Feedback'),
    ('4', 'Done')
]
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=10,choices=TODO_CATEGORY_CHOICES, default='None')
    priority = models.CharField(max_length=15,choices=PRIO_CATEGORY_CHOICES, default='Low')
    user = models.CharField(max_length=120, default='None')
    due_date = models.CharField(max_length=10, default='01-01-2000')
    status = models.CharField(max_length=17,choices=STATUS_CATEGORY_CHOICES, default= 'To do')
    subtasks = models.ManyToManyField(Subtask, default=None)
