# Generated by Django 4.2.16 on 2024-12-15 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfume_list', '0007_perfume_is_available_alter_perfume_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfume',
            name='is_available',
        ),
    ]
