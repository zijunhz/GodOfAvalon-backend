# Generated by Django 4.0.3 on 2022-04-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomstatus',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=7),
        ),
    ]
