from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo, User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email'] #  'user', 'first_name', 'last_name'

class TodoSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'due_date', 'user',  'category'] #'time_passed',


