from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email', 'phone_number', 'enrolled_on')
    search_fields = ('first_name', 'last_name', 'student_id', 'email')

admin.site.register(Student, StudentAdmin)
