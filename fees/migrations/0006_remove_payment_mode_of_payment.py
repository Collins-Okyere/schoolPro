# Generated by Django 5.1.7 on 2025-04-06 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0005_alter_payment_mode_of_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='mode_of_payment',
        ),
    ]
