from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'classes/list_classes.html', {})

def add(request):
    return render(request, 'classes/add_class.html')

def view(request):
    return render(request, 'classes/view_class.html', {})

def edit(request):
    return render(request, 'classes/edit_class.html', {})

def assign(request):
    return render(request, 'classes/assign_class.html', {})


def create(request):
    
    return render(request, 'classes/list_classes.html', {})

def update(request):

    return render(request, 'classes/list_classes.html', {})

def delete(request):

    return render(request, 'classes/list_classes.html', {})

def enroll(request):

    return render(request, 'classes/view_class.html', {})