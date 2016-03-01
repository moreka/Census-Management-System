# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PresenceData',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date_year', models.IntegerField()),
                ('date_month', models.IntegerField()),
                ('date_day', models.IntegerField()),
                ('in_time', models.DateTimeField()),
                ('out_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('username', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='presencedata',
            name='user',
            field=models.ForeignKey(to='presence.User'),
        ),
    ]
