from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='login'),
    path('password/', views.password, name='password'),
    path('new_user/', views.new_user, name='new_user'),
    path('login/', views.login),
    path('change_password/', views.change_password),
    path('create_user/', views.create_user),
]