# Generated by Django 4.2 on 2025-02-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0006_alter_memo_content_alter_memo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='content',
            field=models.TextField(max_length=50),
        ),
    ]
