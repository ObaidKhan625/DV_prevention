# Generated by Django 3.2.9 on 2022-01-17 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20220115_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_document',
            name='user_file_thumbnail',
        ),
    ]
