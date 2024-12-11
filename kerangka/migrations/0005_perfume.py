# Generated by Django 4.2.16 on 2024-12-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kerangka', '0004_userprofile_age_userprofile_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='perfumes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
