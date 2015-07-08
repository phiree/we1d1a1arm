# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('audio_file_path', models.CharField(max_length=200)),
                ('time_begin', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('times_played', models.IntegerField(verbose_name='被推送(播放)的次数')),
                ('is_expired', models.BooleanField(verbose_name='是否已经过期')),
            ],
        ),
    ]
