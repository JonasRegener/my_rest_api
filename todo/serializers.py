from django.contrib.auth.models import User, Group
from rest_framework import serializers, fields
from .models import Todo, User, Subtask

class SubtaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subtask
        fields = [ 'id', 'title' ] #  'subtasks'

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    
    due_date = fields.DateField(input_formats=['%m/%d/%Y'])
    subtasks = SubtaskSerializer(many=True, read_only=False)
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',  'category', 'priority',  'user','due_date', 'status', 'subtasks'] #  'subtasks'
    
    









#""" class SubtasksSerializer(serializers.HyperlinkedModelSerializer):
#
#    subtasks = serializers.PrimaryKeyRelatedField()
#
#    class Meta:
#        model = Subtask """
        


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#
#   class Meta:
#       model = User
#       fields = ['id', 'email'] #  'user', 'first_name', 'last_name'


#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())