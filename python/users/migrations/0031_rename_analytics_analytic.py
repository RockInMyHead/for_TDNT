# Generated by Django 4.1.7 on 2023-04-22 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_analytics_message_analytics_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Analytics',
            new_name='Analytic',
        ),
    ]