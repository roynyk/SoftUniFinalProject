# Generated by Django 4.2.16 on 2024-12-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Riwayat_transaksi', '0003_transactionhistory_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionhistory',
            name='date',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
