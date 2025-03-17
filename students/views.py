from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'students/list_students.html', {})

def add(request):
    return render(request, 'students/add_student.html')

def view(request):
    return render(request, 'students/view_student.html')

def edit(request):
    return render(request, 'students/edit_student.html')

def assign(request):
    return render(request, 'students/assign_student.html')


def create(request):
    
    return render(request, 'students/list_students.html', {})

def update(request):

    return render(request, 'students/list_students.html', {})

def delete(request):

    return render(request, 'students/list_students.html', {})

def enroll(request):

    return render(request, 'students/view_student.html', {})

