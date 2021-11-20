# Generated by Django 3.2.9 on 2021-11-10 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_files', models.ImageField(null=True, upload_to='identity')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='identity_documents',
        ),
        migrations.DeleteModel(
            name='Extra',
        ),
        migrations.AddField(
            model_name='user_documents',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]