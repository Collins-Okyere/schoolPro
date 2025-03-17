from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fees/pay_fees.html', {})


def list_fee_items(request):
    return render(request, 'fees/list_fee_items.html', {})

def add_fee_item(request):
    return render(request, 'fees/add_fee_item.html')

def edit_fee_item(request):
    return render(request, 'fees/edit_fee_item.html', {})

def create_fee_item(request):
    
    return render(request, 'fees/list.html', {})

def update_fee_item(request):

    return render(request, 'fees/list.html', {})



def bill_student(request):
    return render(request, 'fees/bill_student.html', {})

def edit_bill(request):
    return render(request, 'fees/edit_bill.html', {})

def view_bill(request):
    return render(request, 'fees/view_bill.html', {})

def create_bill(request):
    
    return render(request, 'fees/pay_fees.html', {})

def update_bill(request):

    return render(request, 'fees/pay_fees.html', {})



def view_payments(request):
    return render(request, 'fees/list_all_payments.html', {})

def pay_fee(request):
    return render(request, 'fees/pay_fees.html', {})

def edit_payment(request):
    return render(request, 'fees/edit_payment.html', {})

def view_payment(request):
    return render(request, 'fees/view_payment.html', {})

def create_payment(request):
    
    return render(request, 'fees/receipt.html')

def update_payment(request):

    return render(request, 'fees/receipt.html', {})


