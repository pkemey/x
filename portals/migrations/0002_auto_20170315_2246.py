# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
        ('portals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.EndTermExamPerformance'),
        ),
        migrations.AddField(
            model_name='student',
            name='year_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.Year'),
        ),
    ]
