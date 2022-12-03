from django.contrib.auth.models import User, Group
from rest_framework import serializers, fields
from .models import Todo, User, Subtask
from drf_writable_nested.serializers import WritableNestedModelSerializer

class SubtaskSerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = Subtask
        fields = [ 'id', 'title' ] #  'subtasks'

class TodoSerializer(WritableNestedModelSerializer):
    
    due_date = fields.DateField(input_formats=['%m/%d/%Y'])
    subtasks = SubtaskSerializer(many=True) # , read_only=True
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',  'category', 'priority',  'user','due_date', 'status', 'subtasks'] #  'subtasks'