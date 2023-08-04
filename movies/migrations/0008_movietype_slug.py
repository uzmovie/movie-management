# Generated by Django 4.2.3 on 2023-08-04 13:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_actor_movie_actors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movietype',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='movie', editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
