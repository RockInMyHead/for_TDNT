# Generated by Django 4.1.7 on 2023-03-27 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_code_quantity_name_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quantity',
            name='user',
        ),
    ]
