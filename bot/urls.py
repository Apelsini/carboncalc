from django.urls import path

from . import views
from .views import create_view

#https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/

urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),
    path('bot/', view=views.IndexView.as_view(), name='index'),
    path('add/', view=create_view, name='add'),
    path('c19/', views.c19, name='c19'),
    path('c19cd/', views.c19cd, name='c19cd'),
]