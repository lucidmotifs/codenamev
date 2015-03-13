# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplayer', '0006_auto_20150305_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='filename',
            field=models.FileField(upload_to=b''),
            preserve_default=True,
        ),
    ]
