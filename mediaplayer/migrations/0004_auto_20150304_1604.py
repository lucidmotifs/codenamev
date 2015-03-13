# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplayer', '0003_episode_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video_name',
            new_name='title',
        ),
    ]
