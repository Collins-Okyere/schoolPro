from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/list_courses.html', {'courses': courses})

def add(request):
    return render(request, 'courses/add_course.html')

def view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/view_course.html', {'course': course})

def edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/edit_course.html', {'course': course})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        new_course = Course.objects.create(name=name, code=code)
        return redirect('courses:list')

def update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.name = request.POST['name']
        course.code = request.POST['code']
        course.save()
        return redirect('courses:list')
    return render(request, 'courses/edit_course.html', {'course': course})

def delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('courses:list')
