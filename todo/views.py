from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from .models import Todo, Subtask
from .serializers import TodoSerializer, SubtaskSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User
import json


# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-due_date')
    serializer_class = TodoSerializer
    
    def create(self, request):
        todo = Todo.objects.create(title = request.POST.get('title',''),
                                    description = request.POST.get('description', ''), 
                                    category = request.POST.get('category', 'none'),
                                    priority = request.POST.get('priority', 'low'),
                                    user= request.POST.get('user', ''),
                                    due_date= request.POST.get('due_date','01-01-2000'),
                                    status= request.POST.get('status', 'To do'),
                                    subtasks= request.POST.get('subtasks', 'abc'),
                                    )
        serzialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serzialized_obj, content_type='application/json')

class SubtaskViewSet(viewsets.ModelViewSet): 
    queryset = Subtask.objects.all().order_by('-title')
    serializer_class = SubtaskSerializer

    def create(self, request):
        subtask = Subtask.objects.create(title = request.POST.get('title', ''),
                                            done = request.POST.get('done', bool),

        )
        serzialized_subtask = serializers.serialize('json', [subtask, ])
        return HttpResponse(serzialized_subtask, content_type='application/json')
        


""" class UserViewSet(viewsets.UserViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data) """