from django.urls import path
from . import views # Импортируем содержимое views.py

urlpatterns = [
  path('', views.index, name = 'index')
]

