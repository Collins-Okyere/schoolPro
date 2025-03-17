from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.index, name='list'),
    path('add/', views.add, name='add'),
    path('view/', views.view, name='view'),
    path('edit/', views.edit, name='edit'),
    path('enroll/', views.enroll, name='enroll'),
    path('create/', views.create),
    path('update/', views.update),
    path('delete/', views.delete),
    path('assign/', views.assign),
]