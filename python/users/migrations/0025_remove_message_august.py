# Generated by Django 4.1.7 on 2023-04-22 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_remove_message_anl_message_august_message_may_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='august',
        ),
    ]