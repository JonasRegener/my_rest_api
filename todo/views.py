from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from .models import Todo, Subtask, Category
from .serializers import TodoSerializer, SubtaskSerializer, CategorySerializer
from django.http import HttpResponse
from django.contrib.auth.models import User
import json


# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-due_date')
    serializer_class = TodoSerializer


def create(self, request):
    if request.method == 'POST':
        """
        This is a view to create an Todo.
        """
        new_todo = Todo.objects.create(
            title=request.POST['title'], 
            description=request.POST['description'], 
            categories=request.POST['categories'],
            priority=request.POST['priority'], 
            user=request.POST['user'], 
            due_date=request.POST['due_date'], 
            status=request.POST['status'], 
            subtasks=request.POST['title'])
        new_todo.save()


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all().order_by('-title')
    serializer_class = SubtaskSerializer

    def create(self, request):
        """
        This is a view to create an Subtask.
        """
        subtask = Subtask.objects.create(
            title=request.POST.get('title', ''),
            done=request.POST.get('done', 'false'),
            )
        serzialized_subtask = serializers.serialize('json', [subtask, ])
        return HttpResponse(serzialized_subtask, content_type='application/json')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-title')
    serializer_class = CategorySerializer

    def create(self, request):
        """
        This is a view to create an Category.
        """
        category = Category.objects.create(
            title=request.POST.get('title', ''),
            color=request.POST.get('color', '')
            )
        serzialized_category = serializers.serialize('json', [category, ])
        return HttpResponse(serzialized_category, content_type='application/json')



