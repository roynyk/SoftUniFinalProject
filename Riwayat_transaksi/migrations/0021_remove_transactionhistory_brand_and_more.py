# Generated by Django 4.2.16 on 2024-12-15 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Riwayat_transaksi', '0020_remove_transactionhistory_bukti_transaksi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionhistory',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='transactionhistory',
            name='date',
        ),
        migrations.RemoveField(
            model_name='transactionhistory',
            name='payment_method',
        ),
    ]
