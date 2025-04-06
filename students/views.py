from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from classrooms.models import Classroom
from courses.models import Course

def index(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

def add(request):
    gender_list = ['Male', 'Female']
    classrooms = Classroom.objects.all()
    courses = Course.objects.all()
    return render(request, 'students/add_student.html', {'classrooms': classrooms, 'courses': courses, 'gender_list': gender_list})

def view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/view_student.html', {'student': student})

def edit(request, pk):
    gender_list = ['Male', 'Female']
    student = get_object_or_404(Student, pk=pk)
    classrooms = Classroom.objects.all()
    courses = Course.objects.all()
    return render(request, 'students/edit_student.html', {'student': student, 'classrooms': classrooms, 'courses': courses, 'gender_list': gender_list})

def generate_student_id(student):
    initials = (student.first_name[0].upper() + student.last_name[0].upper())
    number = str(Student.objects.count() + 1).zfill(3)
    student_id = f"{initials}-{number}"
    while Student.objects.filter(student_id=student_id).exists():
        number = str(int(number) + 1).zfill(3)
        student_id = f"{initials}-{number}"
    return student_id

def create(request):
    if request.method == 'POST':
        classroom_id = request.POST.get('classroom')
        course_id = request.POST.get('course')
        classroom = get_object_or_404(Classroom, pk=classroom_id)
        course = get_object_or_404(Course, pk=course_id)
        student = Student(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            email=request.POST.get('email'),
            date_of_birth = request.POST.get('date_of_birth'),
            phone_number=request.POST.get('phone_number'),
            classroom=classroom,
            course=course
        )
        student.student_id = generate_student_id(student)
        student.save()
        return redirect('students:list')

def update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.gender = request.POST['gender']
        student.email = request.POST.get('email', '')
        student.phone_number = request.POST.get('phone_number', '')
        student.date_of_birth = request.POST.get('date_of_birth')
        course_id = request.POST.get('course')
        classroom_id = request.POST.get('classroom')
        student.course = get_object_or_404(Course, pk=course_id)
        student.classroom = get_object_or_404(Classroom, pk=classroom_id)
        student.save()
        return redirect('students:view', pk=student.pk)

def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')
