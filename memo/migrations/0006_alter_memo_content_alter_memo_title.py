# Generated by Django 4.2 on 2025-02-10 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0005_alter_memo_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='content',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='memo',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
