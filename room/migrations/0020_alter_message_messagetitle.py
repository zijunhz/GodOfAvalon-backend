# Generated by Django 4.0.3 on 2022-04-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0019_user_voted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messagetitle',
            field=models.CharField(max_length=200),
        ),
    ]
