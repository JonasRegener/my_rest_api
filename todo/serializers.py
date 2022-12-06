from django.contrib.auth.models import User, Group
from rest_framework import serializers, fields
from .models import Todo, User, Subtask, Category
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField


class CategorySerializer(WritableNestedModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'color']  # 'subtasks'


class SubtaskSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Subtask
        fields = ['id', 'title', 'done']  # 'subtasks'

class SubtaskField(serializers.Field):
    """
    Subtask objects are serialized into 'Subtask(title)' notation.
    """
    def to_representation(self, value):
        return "Subtask(%d)" % (value.title, value.done)

class CategoryField(serializers.Field):
    """
    Subtask objects are serialized into 'Category(title' notation.
    """
    def to_representation(self, value):
        return "Category(%d)" % (value.title, value)

class TodoSerializer(serializers.ModelSerializer):

    #tags = StringArrayField()
    categories = PresentablePrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        presentation_serializer=CategorySerializer,
        presentation_serializer_kwargs={
            'example': [
                'of',
                'passing',
                'kwargs',
                'to',
                'serializer',
            ]
        },
        read_source=None
    )
    due_date = fields.DateField(input_formats=['%d/%m/%Y'])
    subtasks = PresentablePrimaryKeyRelatedField(
        queryset=Subtask.objects.all(),
        presentation_serializer=SubtaskSerializer,
        presentation_serializer_kwargs={
            'example': [
                'of',
                'passing',
                'kwargs',
                'to',
                'serializer',
            ]
        },
        read_source=None
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',  'categories', 'priority',
                  'user', 'due_date', 'status', 'subtasks']  
