# Generated by Django 4.1.7 on 2023-04-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_remove_analytic_send_email_alter_analytic_open_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytic',
            name='send_email',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]