# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-12 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(editable=False, max_length=128, unique=True, verbose_name='key')),
                ('secret', models.CharField(editable=False, max_length=128, verbose_name='secret')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'verbose_name_plural': 'API accesses',
                'verbose_name': 'API access',
            },
        ),
        migrations.CreateModel(
            name='APIPermissionGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('groups', models.ManyToManyField(related_name='api_permissions', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name_plural': 'API permissions groups',
                'verbose_name': 'API permission group',
            },
        ),
        migrations.CreateModel(
            name='APIPermissionScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=250, unique=True, verbose_name='Permission scope identifier')),
            ],
            options={
                'verbose_name_plural': 'API permission scopes',
                'verbose_name': 'API permission scope',
            },
        ),
        migrations.AddField(
            model_name='apipermissiongroups',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='shuup_api_permission.APIPermissionScope', verbose_name='permissions'),
        ),
        migrations.AddField(
            model_name='apiaccess',
            name='anonymous_permissions',
            field=models.ManyToManyField(blank=True, to='shuup_api_permission.APIPermissionScope', verbose_name='anonymous permissions'),
        ),
        migrations.AddField(
            model_name='apiaccess',
            name='permissions_groups',
            field=models.ManyToManyField(blank=True, to='shuup_api_permission.APIPermissionGroups', verbose_name='API permission groups'),
        ),
    ]
