# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplayer', '0004_auto_20150304_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('votes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(verbose_name=b'Created')),
                ('modified', models.DateTimeField(verbose_name=b'Modified')),
                ('video', models.ForeignKey(to='mediaplayer.Video')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
