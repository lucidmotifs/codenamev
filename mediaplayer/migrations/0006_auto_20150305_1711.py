# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplayer', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='creator',
            field=models.ForeignKey(default=1, to='mediaplayer.Creator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='filename',
            field=models.CharField(default='Big_Buck_Bunny_Trailer.m4v', max_length=64),
            preserve_default=False,
        ),
    ]
