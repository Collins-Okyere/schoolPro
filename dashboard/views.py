from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'dashboard/student_dashboard.html', {})

def teacher(request):

    return render(request, 'dashboard/teacher_dashboard.html', {})

def admin(request):

    return render(request, 'dashboard/admin_dashboard.html', {})