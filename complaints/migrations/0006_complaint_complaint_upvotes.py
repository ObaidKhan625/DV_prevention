# Generated by Django 3.2.9 on 2022-02-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0005_remove_complaint_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaint_upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
