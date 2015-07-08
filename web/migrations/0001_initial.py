# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio_sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('loginname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('ownerof', models.ForeignKey(help_text='该用户登录时会自动跳转到该频道', verbose_name='频道拥有者', to='radio_sites.RadioSite')),
            ],
        ),
    ]
