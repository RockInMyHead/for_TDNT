# Generated by Django 4.1.7 on 2023-03-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]