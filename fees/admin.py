from django.contrib import admin
from .models import Student, Fee, Payment

class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('student__first_name', 'student__last_name', 'student__student_id')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'date', 'mode_of_payment', 'status')
    list_filter = ('status', 'date')
    search_fields = ('student__first_name', 'student__last_name', 'student__student_id', 'mode_of_payment')

admin.site.register(Fee, FeeAdmin)
admin.site.register(Payment, PaymentAdmin)
