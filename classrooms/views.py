from django.shortcuts import render, get_object_or_404, redirect
from classrooms.models import Classroom

def index(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classrooms/list_classrooms.html', {'classrooms': classrooms})

def add(request):
    return render(request, 'classrooms/add_classroom.html')

def view(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    return render(request, 'classrooms/view_classroom.html', {'classroom': classroom})

def edit(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    return render(request, 'classrooms/edit_classroom.html', {'classroom': classroom})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        new_classroom = Classroom.objects.create(name=name, code=code)
        return redirect('classrooms:list')

def update(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        classroom.name = request.POST['name']
        classroom.code = request.POST['code']
        classroom.save()
        return redirect('classrooms:list')
    return render(request, 'classrooms/edit_classroom.html', {'classroom': classroom})

def delete(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    classroom.delete()
    return redirect('classrooms:list')
