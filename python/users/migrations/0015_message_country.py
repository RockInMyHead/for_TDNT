# Generated by Django 4.1.7 on 2023-03-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_quantity_user_message_open_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='country',
            field=models.CharField(default=1, max_length=20000),
            preserve_default=False,
        ),
    ]
