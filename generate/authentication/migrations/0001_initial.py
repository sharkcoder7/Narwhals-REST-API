# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('position', models.IntegerField(help_text='Ranking position.', null=True, verbose_name='Ranking position.', blank=True)),
                ('meters', models.IntegerField(help_text='Total meters.', null=True, verbose_name='Total meters.', blank=True)),
                ('minutes', models.IntegerField(help_text='Total minutes.', null=True, verbose_name='Total minutes.', blank=True)),
                ('strokes', models.IntegerField(help_text='Total strokes', null=True, verbose_name='Total strokes.', blank=True)),
                ('metersAverage', models.IntegerField(help_text='Meters average.', null=True, verbose_name='Meters average.', blank=True)),
                ('minutesAverage', models.IntegerField(help_text='Minutes average', null=True, verbose_name='Minutes average.', blank=True)),
                ('city_id', models.IntegerField(help_text='??', null=True, verbose_name='??', blank=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('surname', models.CharField(max_length=100, null=True, blank=True)),
                ('trend', models.CharField(default=b'down', max_length=10, choices=[(b'up', b'UP'), (b'down', b'DOWN')])),
                ('bio', models.CharField(max_length=500, null=True, blank=True)),
                ('avatar', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
