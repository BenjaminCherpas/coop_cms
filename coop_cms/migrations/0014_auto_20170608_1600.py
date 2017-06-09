# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0013_auto_20170607_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alias',
            name='redirect_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=100, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='fragmenttype',
            name='allowed_css_classes',
            field=models.CharField(default='', help_text='the css classed proposed when editing a fragment. It must be separated by comas', max_length=200, verbose_name='allowed css classes'),
        ),
        migrations.AlterField(
            model_name='image',
            name='copyright',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='copyright'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='imagesize',
            name='crop',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='crop'),
        ),
        migrations.AlterField(
            model_name='navtree',
            name='name',
            field=models.CharField(db_index=True, default='default', max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='navtype',
            name='search_field',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='search field'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=models.TextField(blank=True, default='<br>', verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='source_url',
            field=models.URLField(blank=True, default='', verbose_name='source url'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='subject',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='template',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='template'),
        ),
        migrations.AlterField(
            model_name='pieceofhtml',
            name='content',
            field=models.TextField(blank=True, default='', verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='pieceofhtml',
            name='extra_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=100, verbose_name='extra identifier'),
        ),
    ]
