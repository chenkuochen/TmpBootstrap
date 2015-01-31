# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('photo', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=30)),
                ('photo', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendance_num', models.IntegerField()),
                ('available_num', models.IntegerField()),
                ('price', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to=b'')),
                ('pet', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('wine', models.BooleanField(default=False)),
                ('attendance', models.ManyToManyField(related_name='attendance_table', to='restfulAPI.Person')),
                ('host', models.ForeignKey(to='restfulAPI.Person')),
                ('location', models.ForeignKey(to='restfulAPI.Location')),
                ('menu', models.ManyToManyField(to='restfulAPI.Meal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
