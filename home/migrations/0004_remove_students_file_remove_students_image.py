# Generated by Django 5.1.4 on 2025-03-30 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_students_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='file',
        ),
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
    ]
