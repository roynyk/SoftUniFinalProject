# Generated by Django 4.2.16 on 2024-12-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume_list', '0005_alter_perfume_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfume',
            name='name',
            field=models.CharField(default='Unnamed Perfume', max_length=255),
        ),
        migrations.AddField(
            model_name='perfume',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
