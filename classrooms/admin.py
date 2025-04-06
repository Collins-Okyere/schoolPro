from django.contrib import admin
from .models import Classroom

# Class Admin Configuration
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')  # Columns to display in the list view
    search_fields = ('name', 'code')  # Fields to search by
    ordering = ('name',)  # Default ordering by name

# Registering the models in the admin site
admin.site.register(Classroom, ClassroomAdmin)
