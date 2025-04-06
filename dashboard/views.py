from django.shortcuts import render
from classrooms.models import Classroom
from fees.models import Payment
from students.models import Student
from courses.models import Course

def index(request):
    students_count = Student.objects.count()
    courses_count = Course.objects.count()
    classes_count = Classroom.objects.count()
    payments = Payment.objects.all()
    context = {
        'students_count': students_count,
        'courses_count': courses_count,
        'classes_count': classes_count,
        'payments': payments
    }

    return render(request, 'dashboard/dashboard.html', context)
