# Generated by Django 4.2 on 2025-02-06 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='memo',
            name='updated_at',
        ),
    ]
