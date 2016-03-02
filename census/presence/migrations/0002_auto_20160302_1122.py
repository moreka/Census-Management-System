# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='presencedata',
            unique_together=set([('user', 'date_year', 'date_month', 'date_day')]),
        ),
    ]
