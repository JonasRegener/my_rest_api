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
    if request.method == 'GET':
        todo = Todo.objects.create(title = request.POST.get('title',''),
        description = request.POST.get('description', ''), 
        category = request.POST.get('category', 'none'),
        priority = request.POST.get('priority', 'low'),
        user= request.POST.get('user', ''),
        due_date= request.POST.get('due_date','01-01-2000'),
        status= request.POST.get('status', 'To do'),subtasks= request.POST.get('subtasks', ''),
        )
        serzialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serzialized_obj, content_type='application/json')
    if request.method == 'POST':
        new_todo = Todo.objects.create(title=request.POST['title'], description=request.POST['description'], category=request.POST['category'], priority=request.POST['priority'], user=request.POST['user'],due_date=request.POST['due_date'],status=request.POST['status'], subtasks=request.POST['title'])
        new_todo.save()

def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks')
        instance = super(TodoSerializer, self).update(instance, validated_data)

        for subtask_data in subtasks_data:
            subtasks_qs = Subtask.objects.filter(name__iexact=subtask_data['title'])

            if subtasks_qs.exists():
                subtasks = subtasks_qs.first()
            else: subtasks = Subtask.objects.create(**subtask_data)

            instance.subtasks.add(subtasks)
        
        return instance


class SubtaskViewSet(viewsets.ModelViewSet): 
    queryset = Subtask.objects.all().order_by('-title')
    serializer_class = SubtaskSerializer

    def create(self, request):
        subtask = Subtask.objects.create(title = request.POST.get('title', ''),
        )
        serzialized_subtask = serializers.serialize('json', [subtask, ])
        return HttpResponse(serzialized_subtask, content_type='application/json')
        
