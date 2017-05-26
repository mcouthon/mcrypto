# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('crypto', models.BooleanField(default=True))
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=0.0)),
                ('base', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='base', to='portfolio.Currency')),
                ('target', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='target', to='portfolio.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('amount', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='portfolio.Amount')),
                ('asset', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='portfolio.Asset')),
            ],
        ),
        migrations.AddField(
            model_name='amount',
            name='coin',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='portfolio.Currency'),
        ),
    ]
