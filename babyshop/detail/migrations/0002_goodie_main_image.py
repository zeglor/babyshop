# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodie',
            name='main_image',
            field=models.FileField(default='settins.MEDIA_ROOT/placeholder500x500.png', upload_to='main_image/'),
        ),
    ]
