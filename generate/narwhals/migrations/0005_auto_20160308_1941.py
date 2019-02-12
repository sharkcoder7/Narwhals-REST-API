# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('narwhals', '0004_auto_20160308_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='auto_increment_id',
            new_name='id',
        ),
    ]
