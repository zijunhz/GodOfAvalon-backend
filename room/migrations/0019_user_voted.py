# Generated by Django 4.0.3 on 2022-04-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0018_room_teambuilder_room_teammembercount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='voted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
