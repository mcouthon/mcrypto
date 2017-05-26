# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Currency, Asset, Holding
from .forms import HoldingForm


# Create your views here.
class IndexView(ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'currency_list'

    def get_queryset(self):
        return Currency.objects.all()


class AssetView(DetailView):
    model = Asset
    template_name = 'portfolio/asset.html'


class HoldingView(DetailView):
    model = Holding
    template_name = 'portfolio/holding.html'


class CurrencyView(DetailView):
    model = Currency
    template_name = 'portfolio/currency.html'


def edit_holding(request, pk):
    holding = get_object_or_404(Holding, pk=pk)
    holding_form = HoldingForm(instance=holding)
    return render(request, 'portfolio/edit_holding.html',
                  {'holding_form': holding_form})
