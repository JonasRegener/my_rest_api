from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date, timedelta


class Category(models.Model):
    """ Many to Many - Model for Todo"""
    title = models.CharField(max_length=30)
    color = models.CharField(max_length=30)


class Subtask(models.Model):
    """ Many to Many - Model for Todo"""
    title = models.CharField(max_length=30)
    done = models.CharField(max_length=30, default='False')


class Todo(models.Model):
    """ Main Model """
    PRIO_CATEGORY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    ]
    STATUS_CATEGORY_CHOICES = [
        ('1', 'To do'),
        ('2', 'In progress'),
        ('3', 'Awaiting Feedback'),
        ('4', 'Done'),
        ('5', 'Deleted')
    ]
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category, default=None)
    priority = models.CharField(max_length=15, choices=PRIO_CATEGORY_CHOICES, default='Low')
    user = models.CharField(max_length=120, default='None')
    due_date = models.DateField(max_length=10, default='01-01-2000')
    status = models.CharField(max_length=17, choices=STATUS_CATEGORY_CHOICES, default='To do')
    subtasks = models.ManyToManyField(Subtask, default=None)
