# Generated by Django 4.2.16 on 2024-12-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0009_alter_payment_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bukti_transaksi',
            field=models.ImageField(blank=True, null=True, upload_to='bukti_transaksi/'),
        ),
    ]
