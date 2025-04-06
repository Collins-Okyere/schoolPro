from django.shortcuts import redirect, render

# Create your views here.

def login(request):
    return redirect('dashboard:index')


def register(request):
    return render(request, 'authentication/register.html')

def logout(request):
    return render(request, 'authentication/login.html')
