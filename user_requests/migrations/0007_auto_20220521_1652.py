# Generated by Django 3.2.9 on 2022-05-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_requests', '0006_rename_complaint_complaint_request_requested_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint_request',
            name='request_read',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact_request',
            name='request_read',
            field=models.BooleanField(default=True),
        ),
    ]
