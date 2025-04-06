from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='list'),
    path('add/', views.add, name='add'),
    path('<int:pk>/view/', views.view, name='view'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]
