# Generated by Django 3.2.9 on 2021-11-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20211111_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile_image',
            field=models.ImageField(default='profiles/default-images.jpg', null=True, upload_to='profiles'),
        ),
    ]