# Generated by Django 4.2.16 on 2024-12-15 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0010_payment_bukti_transaksi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='bukti_transaksi',
        ),
    ]
