# Generated by Django 3.2.9 on 2022-03-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0018_complaint_complaint_abc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaint_abc',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
