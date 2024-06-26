# Generated by Django 4.1.7 on 2023-04-22 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_remove_message_anl_delete_analitic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analitic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('august', models.IntegerField(default=0, null=True)),
                ('may', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='anl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.analitic'),
        ),
    ]
