# Generated by Django 4.1.7 on 2023-03-29 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0011_message_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]