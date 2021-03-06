# Generated by Django 3.2.9 on 2021-11-29 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_rename_contact_requests_contact_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_other',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Contact_Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permitted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permitted_by_permissions', to=settings.AUTH_USER_MODEL)),
                ('permitted_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permitted_user_permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
