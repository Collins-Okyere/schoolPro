from django.urls import path
from . import views

app_name = 'fees'

urlpatterns = [
    
    path('fee_items/', views.list_fee_items, name='fee_items'),
    path('add_fee_item/', views.add_fee_item, name='add_fee_item'),
    path('edit_fee_item/', views.edit_fee_item, name='edit_fee_item'),
    path('create_fee_item/', views.create_fee_item),
    path('update_fee_item/', views.update_fee_item),

    path('bill_student/', views.bill_student, name='bill_student'),
    path('edit_bill/', views.edit_bill, name='edit_bill'),
    path('view_bill/', views.view_bill, name='aview_bill'),
    path('create_bill/', views.create_bill),
    path('update_bill/', views.update_bill),
    
    path('', views.index, name='pay_fee'),
    path('view_payments/', views.view_payments, name='view_payments'),
    path('pay_fee/', views.pay_fee, name='pay_fee'),
    path('edit_payment/', views.edit_payment, name='edit_payment'),
    path('view_payment/', views.view_payment, name='view_payment'),
    path('create_payment/', views.create_payment),
    path('update_payment/', views.update_payment),

]