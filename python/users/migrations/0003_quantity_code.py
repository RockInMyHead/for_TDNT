# Generated by Django 4.1.7 on 2023-03-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='code',
            field=models.CharField(default=1, max_length=20000),
            preserve_default=False,
        ),
    ]
