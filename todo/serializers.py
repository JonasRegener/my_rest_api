from django.contrib.auth.models import User, Group
from rest_framework import serializers, fields
from .models import Todo, User



class TodoSerializer(serializers.HyperlinkedModelSerializer):

    due_date = fields.DateField(input_formats=['%m/%d/%Y'])

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',  'category', 'priority',  'user','due_date'] 


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#
#   class Meta:
#       model = User
#       fields = ['id', 'email'] #  'user', 'first_name', 'last_name'


#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())