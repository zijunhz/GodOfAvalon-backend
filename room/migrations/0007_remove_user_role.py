# Generated by Django 4.0.3 on 2022-04-02 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
