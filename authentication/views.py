from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'authentication/login.html')

def password(request):
    return render(request, 'authentication/change_password.html', {})

def new_user(request):
    return render(request, 'authentication/create_user.html')

def login(request):

    return render(request, 'dashboard/dashboard.html', {})

def change_password(request):

    return render(request, 'authentication/login.html')

def create_user(request):

    return render(request, 'authentication/login.html')
