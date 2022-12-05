from django.contrib.auth.models import User, Group
from rest_framework import serializers, fields
from .models import Todo, User, Subtask, Category
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = Category
        fields = [ 'id', 'title', 'color' ] #  'subtasks'

class SubtaskSerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = Subtask
        fields = [ 'id', 'title', 'done' ] #  'subtasks'

class TodoSerializer(WritableNestedModelSerializer):

    categories = CategorySerializer(many=True)
    due_date = fields.DateField(input_formats=['%m/%d/%Y'])
    subtasks = SubtaskSerializer(many=True) # , read_only=True
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',  'categories', 'priority',  'user','due_date', 'status', 'subtasks'] #  'subtasks'