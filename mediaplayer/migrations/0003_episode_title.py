# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplayer', '0002_auto_20150211_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='title',
            field=models.CharField(default='Pilot', max_length=50),
            preserve_default=False,
        ),
    ]
