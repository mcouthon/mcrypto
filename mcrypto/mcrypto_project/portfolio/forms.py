from django.forms import ModelForm

from . import models


class CurrencyForm(ModelForm):
    class Meta:
        model = models.Currency
        fields = ['code', 'name']


class ExchangeRateForm(ModelForm):
    class Meta:
        model = models.ExchangeRate
        fields = ['base', 'target', 'rate']


class AssetForm(ModelForm):
    class Meta:
        model = models.Asset
        fields = ['code', 'name']


class AmountForm(ModelForm):
    class Meta:
        model = models.Amount
        fields = ['coin', 'amount']


class HoldingForm(ModelForm):
    class Meta:
        model = models.Holding
        fields = ['asset', 'amount']
