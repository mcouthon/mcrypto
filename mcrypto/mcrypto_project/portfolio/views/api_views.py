from django.shortcuts import render
from django.views.generic import TemplateView

from .. import apis
from .mixins import LoginRequiredMixin


class BaseUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio/index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context=context)


class CurrencyUpdateView(BaseUpdateView):
    def get_context_data(self, **kwargs):
        context = super(CurrencyUpdateView, self).get_context_data(**kwargs)
        return context


class ExchangeUpdateView(BaseUpdateView):
    def get_context_data(self, **kwargs):
        context = super(ExchangeUpdateView, self).get_context_data(**kwargs)

        return context


class CryptoExchangeUpdateView(BaseUpdateView):
    def get_context_data(self, **kwargs):
        context = super(CryptoExchangeUpdateView, self).get_context_data(
            **kwargs)
        context.update(apis.get_exchange_rates())
        return context
