from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'courses/list_courses.html', {})

def add(request):
    return render(request, 'courses/add_course.html')

def view(request):
    return render(request, 'courses/view_course.html')

def edit(request):
    return render(request, 'courses/edit_course.html')

def assign(request):
    return render(request, 'courses/assign_course.html')



def create(request):
    
    return render(request, 'courses/list_courses.html', {})

def update(request):

    return render(request, 'courses/list_courses.html', {})

def delete(request):

    return render(request, 'courses/list_courses.html', {})

def enroll(request):

    return render(request, 'courses/view_courses.html', {})