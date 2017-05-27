from django.views.generic import DetailView

from ..models import Currency


class CurrencyDetail(DetailView):
    model = Currency
    template_name = 'portfolio/currency/detail.html'
