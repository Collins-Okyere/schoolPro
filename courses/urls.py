from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='list'),
    path('add/', views.add, name='add'),
    path('<int:pk>/', views.view, name='view'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
