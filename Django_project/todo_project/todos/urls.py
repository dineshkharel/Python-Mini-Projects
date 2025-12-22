from django.urls import path
from .views import TodoListCreateAPIView

urlpatterns=[
    path('todos/', TodoListCreateAPIView.as_view())
]