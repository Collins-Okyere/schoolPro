from django.db import models
from django.utils import timezone

from students.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, related_name='fees', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Fee for {self.student.first_name} {self.student.last_name} - {self.amount}"


class Payment(models.Model):
    student = models.ForeignKey(Student, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    mode_of_payment = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=20, default='Paid')
