# Generated by Django 4.2.16 on 2024-12-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Riwayat_transaksi', '0007_remove_transactionhistory_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionhistory',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
