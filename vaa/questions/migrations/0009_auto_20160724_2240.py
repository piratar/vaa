# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20160720_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=b'/var/www/vaamedia/cand_pics'),
        ),
    ]
