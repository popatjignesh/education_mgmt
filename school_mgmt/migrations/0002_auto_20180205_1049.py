# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='SMARTNumber',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'school_logo/', blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='university',
            field=models.ForeignKey(related_name=b'schools', to='school_mgmt.University'),
        ),
    ]
