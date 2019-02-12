# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sport', models.CharField(blank=True, max_length=1, null=True, choices=[(b'0', b'natacion'), (b'1', b'ciclismo'), (b'2', b'senderismo')])),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('dateStart', models.DateTimeField(auto_now_add=True, help_text='Date of the creation', null=True, verbose_name='Creation date')),
                ('dateEnd', models.DateTimeField(auto_now_add=True, help_text='End date', null=True, verbose_name='End date')),
                ('duration', models.IntegerField(help_text='Duration of the training', null=True, verbose_name='Duration of the training', blank=True)),
                ('distance', models.FloatField(help_text='Distance of the training', null=True, verbose_name='Distance of the training', blank=True)),
                ('speedMax', models.FloatField(help_text='Max speed peak in meters', null=True, verbose_name='Max speed peak in meters', blank=True)),
                ('speedAvg', models.FloatField(help_text='Average speed in meter/seconds', null=True, verbose_name='Average speed in meter/seconds', blank=True)),
                ('heightMax', models.IntegerField(help_text='Min height in meters', null=True, verbose_name='Max height in meters', blank=True)),
                ('heightMin', models.IntegerField(help_text='Duration of the training', null=True, verbose_name='Duration of the training', blank=True)),
                ('metersUploaded', models.IntegerField(help_text='Total uploaded meters', null=True, verbose_name='Total uploaded meters', blank=True)),
                ('metersDownloaded', models.IntegerField(help_text='Total downloaded meters', null=True, verbose_name='Total downloaded meters', blank=True)),
                ('filetype', models.CharField(blank=True, max_length=1, null=True, choices=[(b'0', b'gps'), (b'1', b'axis')])),
                ('filepath', models.CharField(default=b'', max_length=500, null=True, blank=True)),
                ('isPrivate', models.BooleanField(default=False, help_text='Private (y/n)?', verbose_name='Private')),
                ('isSynchronized', models.BooleanField(default=False, help_text='Synchronized (y/n)?', verbose_name='Synchronizes')),
                ('difficulty', models.IntegerField(default=1, help_text='Difficulty of the training', null=True, verbose_name='Difficulty of the training', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
