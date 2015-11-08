# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('short_url', models.URLField(unique=True)),
                ('target_url', models.URLField()),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
