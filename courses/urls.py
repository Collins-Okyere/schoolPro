from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='list'),
    path('add/', views.add, name='add'),
    path('view/', views.view, name='view'),
    path('edit/', views.edit, name='edit'),
    path('assign/', views.assign, name='assign'),
    path('enroll/', views.enroll),
    path('create/', views.create),
    path('update/', views.update),
    path('delete/', views.delete),
]