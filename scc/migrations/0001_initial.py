# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ISAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.TextField(blank=True, null=True)),
                ('objective', models.TextField(blank=True, null=True)),
                ('method', models.TextField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('conclusion', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ISSpeaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/speakers/')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(max_length=70)),
                ('affiliation', models.TextField()),
                ('topic', models.CharField(max_length=250)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('venue', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'SCC Invited Speaker',
            },
        ),
        migrations.CreateModel(
            name='OPAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.TextField(blank=True, null=True)),
                ('objective', models.TextField(blank=True, null=True)),
                ('method', models.TextField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('conclusion', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OPSpeaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/speakers/')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(max_length=70)),
                ('affiliation', models.TextField()),
                ('topic', models.CharField(max_length=250)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('venue', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'SCC Oral Presentation',
            },
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/speakers/')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(max_length=70)),
                ('affiliation', models.TextField()),
                ('topic', models.CharField(max_length=250)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('venue', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'SCC Poster',
            },
        ),
        migrations.CreateModel(
            name='PosterAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.TextField(blank=True, null=True)),
                ('objective', models.TextField(blank=True, null=True)),
                ('method', models.TextField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('conclusion', models.TextField(blank=True, null=True)),
                ('keyword', models.TextField(blank=True, null=True)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scc.Poster', unique=True)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='opabstract',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scc.OPSpeaker', unique=True),
        ),
        migrations.AddField(
            model_name='isabstract',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scc.ISSpeaker', unique=True),
        ),
    ]
