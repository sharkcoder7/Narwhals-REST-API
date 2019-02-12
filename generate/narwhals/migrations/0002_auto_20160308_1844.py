# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('narwhals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('auto_increment_id', models.AutoField(serialize=False, primary_key=True)),
                ('sport', models.CharField(blank=True, max_length=1, null=True, choices=[(b'0', b'swimming'), (b'1', b'cycling'), (b'2', b'hiking')])),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('dateStart', models.DateTimeField(auto_now_add=True, help_text='Date of the creation', null=True, verbose_name='Creation date')),
                ('dateFinish', models.DateTimeField(auto_now_add=True, help_text='End date', null=True, verbose_name='End date')),
                ('duration', models.IntegerField(help_text='Duration of the training', null=True, verbose_name='Duration of the training', blank=True)),
                ('distance', models.FloatField(help_text='Distance of the training', null=True, verbose_name='Distance of the training', blank=True)),
                ('strokes', models.FloatField(help_text='Calculated strokes', null=True, verbose_name='Calculated strokes', blank=True)),
                ('speedAverage', models.FloatField(help_text='Average speed in meter/seconds', null=True, verbose_name='Average speed in meter/seconds', blank=True)),
                ('strokeAverage', models.FloatField(help_text='Average strokes per second', null=True, verbose_name='Average strokes per second', blank=True)),
                ('difficulty', models.IntegerField(default=1, help_text='Difficulty of the training', null=True, verbose_name='Difficulty of the training', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='entrenamiento',
            name='user',
        ),
        migrations.DeleteModel(
            name='Entrenamiento',
        ),
    ]
