
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo.views import TodoViewSet, SubtaskViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet )
router.register(r'subtasks', SubtaskViewSet )
router.register(r'categories', CategoryViewSet )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
