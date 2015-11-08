# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 11, 8, 19, 15, 36, 381560, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.URLField(unique=True, null=True, blank=True),
        ),
    ]
