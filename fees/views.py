from django.utils import timezone
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student, Fee, Payment
from django.db import models

def index(request):
    students = Student.objects.all()
    student_fees = []
    for student in students:
        total_due = Fee.objects.filter(student=student).aggregate(total_due=models.Sum('amount'))['total_due'] or 0
        total_paid = Payment.objects.filter(student=student).aggregate(total_paid=models.Sum('amount'))['total_paid'] or 0
        balance = total_due - total_paid
        status = "Paid" if balance == 0 else "Pending"
        student_fees.append({
            'student': student,
            'bill': total_due,
            'amount_paid': total_paid,
            'balance': balance,
            'status': status,
        })
    return render(request, 'fees/students_fees_list.html', {'student_fees': student_fees})

def view_fee(request, pk):
    student = get_object_or_404(Student, pk=pk)
    fees = Fee.objects.filter(student=student)
    payments = Payment.objects.filter(student=student)
    total_due = fees.aggregate(total_due=models.Sum('amount'))['total_due'] or 0
    total_paid = payments.aggregate(total_paid=models.Sum('amount'))['total_paid'] or 0
    balance = total_due - total_paid
    status = "Paid" if balance == 0 else "Pending"
    return render(request, 'fees/view_fee.html', {
        'student': student,
        'fees': fees,
        'payments': payments,
        'total_due': total_due,
        'total_paid': total_paid,
        'balance': balance,
        'status': status,
    })

def view_payment(request, pk):
    student = get_object_or_404(Student, pk=pk)
    payments = Payment.objects.filter(student=student)
    return render(request, 'fees/view_payment.html', {'student': student, 'payments': payments})

def view_all_payments(request):
    payments = Payment.objects.all()
    return render(request, 'fees/view_all_payments.html', {'payments': payments})

def bill(request):
    students = Student.objects.all()
    return render(request, 'fees/bill_student.html', {'students': students})

def save_bill(request):
    if request.method == 'POST':
        pk = request.POST.get('student')
        amount = Decimal(request.POST.get('amount'))
        due_date = request.POST.get('due_date')
        student = get_object_or_404(Student, pk=pk)
        fee = Fee.objects.create(student=student, amount=amount, due_date=due_date)
        return redirect('fees:list')

def pay_fee(request, pk):
    student = Student.objects.get(id=pk)
    total_fees_due = Fee.objects.filter(student=student).aggregate(total_due=models.Sum('amount'))['total_due'] or 0
    total_paid = Payment.objects.filter(student=student).aggregate(total_paid=models.Sum('amount'))['total_paid'] or 0
    balance = total_fees_due - total_paid
    status = "Paid" if balance == 0 else "Pending"
    context = {
        'student': student,
        'total_fees_due': total_fees_due,
        'total_paid': total_paid,
        'balance': balance,
        'status': status
    }
    return render(request, 'fees/pay_fee.html', context)

def save_fee_payment(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        amount = request.POST.get('amount')
        amount = Decimal(amount)
        mode_of_payment = request.POST.get('mode_of_payment')
        payment = Payment(
            student=student,
            amount=amount,
            date=timezone.now(),
            mode_of_payment=mode_of_payment
        )
        payment.save()
        total_paid = Payment.objects.filter(student=student).aggregate(total_paid=models.Sum('amount'))['total_paid'] or Decimal(0)

        return redirect('fees:receipt', pk=payment.id)


def receipt(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'fees/receipt.html', {'payment': payment})
