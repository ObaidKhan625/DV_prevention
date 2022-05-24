# Generated by Django 3.2.9 on 2022-05-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_user_user_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_session_key',
        ),
        migrations.AddField(
            model_name='user',
            name='user_notifications',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
