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

# finished? = models.BooleanField(default=False)
# oder 5ter status
""" class Subtask(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=10,choices=TODO_CATEGORY_CHOICES, default='None')
    priority = models.CharField(max_length=15,choices=PRIO_CATEGORY_CHOICES, default='Low')
    user = models.CharField(max_length=120, default='None')
    due_date = models.CharField(max_length=10, default='01-01-2000')
    status = models.CharField(max_length=17,choices=STATUS_CATEGORY_CHOICES, default= 'To do')
    todo = models.ForeignKey('Todo',  on_delete=models.CASCADE, default= None) """


# user = models.ForeignKey(
#       User,
#       on_delete=models.CASCADE,
#       default=None
#   )

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