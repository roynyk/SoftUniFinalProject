# Generated by Django 4.2.16 on 2024-12-15 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Riwayat_transaksi', '0015_alter_transactionhistory_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionhistory',
            name='payment_method',
        ),
    ]
