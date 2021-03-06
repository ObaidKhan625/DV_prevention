# Generated by Django 3.2.9 on 2021-11-27 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20211122_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_note', models.TextField(null=True)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_by', to=settings.AUTH_USER_MODEL)),
                ('requested_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
