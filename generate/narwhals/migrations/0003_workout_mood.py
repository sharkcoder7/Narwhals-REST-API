# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('narwhals', '0002_auto_20160308_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='mood',
            field=models.IntegerField(default=1, help_text="User's mood", null=True, verbose_name="User's mood", blank=True),
            preserve_default=True,
        ),
    ]
