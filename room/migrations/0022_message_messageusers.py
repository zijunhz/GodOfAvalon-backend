# Generated by Django 4.0.3 on 2022-04-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0021_alter_message_messagetitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='messageusers',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
