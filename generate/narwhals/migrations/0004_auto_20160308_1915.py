# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('narwhals', '0003_workout_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='dateFinish',
            field=models.DateTimeField(help_text='End date', null=True, verbose_name='End date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='dateStart',
            field=models.DateTimeField(help_text='Date of the creation', null=True, verbose_name='Creation date', blank=True),
            preserve_default=True,
        ),
    ]
