# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio_sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='分类名称')),
                ('description', models.CharField(max_length=2000, verbose_name='分类介绍')),
                ('create_date', models.DateTimeField(verbose_name='创建时间')),
                ('podcastor', models.CharField(max_length=20, verbose_name='播音人')),
                ('ads_image', models.CharField(max_length=200, verbose_name='频道广告图片地址')),
                ('channel_belong_to', models.ForeignKey(to='radio_sites.RadioSite', verbose_name='所属电台')),
            ],
        ),
    ]
