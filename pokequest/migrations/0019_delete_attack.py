# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0018_auto_20150830_1925'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attack',
        ),
    ]
