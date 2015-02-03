# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_name', models.CharField(max_length=200)),
                ('video_rating', models.IntegerField(default=3)),
                ('video_desc', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name=b'data published')),
                ('genre', models.ForeignKey(to='mediaplayer.Genre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
