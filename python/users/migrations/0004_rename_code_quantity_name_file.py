# Generated by Django 4.1.7 on 2023-03-27 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_quantity_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantity',
            old_name='code',
            new_name='name_file',
        ),
    ]
