# Generated by Django 3.2.9 on 2022-02-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0011_alter_complaint_complaint_upvotes_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaint_upvotes_users',
            field=models.JSONField(null=True),
        ),
    ]
