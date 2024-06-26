# Generated by Django 4.1.7 on 2023-04-22 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0028_remove_message_country_remove_message_ip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='country',
            field=models.CharField(default='', max_length=20000, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='ip',
            field=models.CharField(default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='may',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='number',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='open_ip',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='sent_number',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='successfully',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
