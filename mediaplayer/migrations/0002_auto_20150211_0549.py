# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mediaplayer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('created', models.DateTimeField(verbose_name=b'Date Created')),
                ('modified', models.DateTimeField(verbose_name=b'Date Modified')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('pseudo', models.CharField(max_length=50)),
                ('registered', models.DateTimeField(verbose_name=b'Date Registered')),
                ('avatar', models.ImageField(upload_to=b'')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(verbose_name=b'Date Created')),
                ('creator', models.ForeignKey(to='mediaplayer.Creator')),
                ('genre', models.ForeignKey(to='mediaplayer.Genre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to=b'')),
                ('creator', models.ForeignKey(to='mediaplayer.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='show',
            name='studio',
            field=models.ForeignKey(to='mediaplayer.Studio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='season',
            name='show',
            field=models.ForeignKey(to='mediaplayer.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(to='mediaplayer.Season'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(to='mediaplayer.Show'),
            preserve_default=True,
        ),
    ]
