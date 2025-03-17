from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='login'),
    path('api/password/', views.password, name='password'),
    path('api/new_user/', views.new_user, name='new_user'),
    path('api/login/', views.login),
    path('api/change_password/', views.change_password),
    path('api/create_user/', views.create_user),
]