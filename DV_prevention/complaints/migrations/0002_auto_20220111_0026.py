# Generated by Django 3.2.9 on 2022-01-10 18:56

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]