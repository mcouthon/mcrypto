# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Currency(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=40)
    crypto = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('portfolio:currency', kwargs={'pk': self.pk})

    def __str__(self):
        crypto = ' [crypto]' if self.crypto else ''
        return '{0} - {1}{2}'.format(self.code, self.name, crypto)


@python_2_unicode_compatible
class ExchangeRate(models.Model):
    base = models.ForeignKey(Currency, related_name='base',
                             on_delete=models.CASCADE)
    target = models.ForeignKey(Currency, related_name='target',
                               on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return reverse('portfolio:exchange', kwargs={'pk': self.pk})

    def __str__(self):
        return '{0} --> {1} [{2}]'.format(self.base, self.target, self.rate)


@python_2_unicode_compatible
class Asset(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('portfolio:asset', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Holding(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    coin = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return reverse('portfolio:holding', kwargs={'pk': self.pk})

    def __str__(self):
        return '{0} {1} [{1}]'.format(self.amount, self.coin.code, self.asset)
