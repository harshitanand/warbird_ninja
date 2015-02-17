# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users_git_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=100)),
                ('payload', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
