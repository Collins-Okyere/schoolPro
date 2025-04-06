from django.urls import path
from . import views

app_name = 'fees'

urlpatterns = [
    path('', views.index, name='list'),
    path('payments/<int:pk>/', views.view_payment, name='view_payment'),
    path('view_all_payments/', views.view_all_payments, name='view_payments'),
    path('bill/', views.bill, name='bill_student'),
    path('save_bill/', views.save_bill, name='save_bill'),
    path('pay_fee/<int:pk>/', views.pay_fee, name='pay_fee'),
    path('view/<int:pk>/', views.view_fee, name='view_fee'),
    path('receipt/<int:pk>/', views.receipt, name='receipt'),
    path('pay/<int:pk>/', views.save_fee_payment, name='save_fee_payment'),
]
