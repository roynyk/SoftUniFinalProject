# Generated by Django 4.2.16 on 2024-12-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]