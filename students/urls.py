from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('view/', views.view, name='view'),
    path('edit/', views.edit, name='edit'),
    path('assign/', views.assign, name='assign'),
    path('create/', views.create),
    path('update/', views.update),
    path('delete/', views.delete),
    path('enroll', views.enroll),
]