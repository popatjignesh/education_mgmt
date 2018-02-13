# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=15, choices=[(b'india', b'India'), (b'england', b'England'), (b'australia', b'Australia'), (b'united_states', b'United States'), (b'canada', b'Canada'), (b'new_zealand', b'New Zealand')])),
                ('zipcode', models.IntegerField(null=True, blank=True)),
                ('mobile', models.BigIntegerField(max_length=13, null=True, verbose_name=b'Mobile No.', blank=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'School Name')),
                ('logo', models.ImageField(upload_to=b'school_logo/')),
                ('website', models.CharField(max_length=50, null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'School',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('roll_no', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.ManyToManyField(to='school_mgmt.Address')),
                ('school', models.ForeignKey(to='school_mgmt.School')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Student',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'University Name')),
                ('logo', models.ImageField(upload_to=b'university_logo/')),
                ('website', models.CharField(max_length=50, null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'University',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='school',
            name='university',
            field=models.ForeignKey(to='school_mgmt.University'),
            preserve_default=True,
        ),
    ]
