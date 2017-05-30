from django.views.generic import DetailView

from ..models import Currency
from .mixins import LoginRequiredMixin


class CurrencyDetail(LoginRequiredMixin, DetailView):
    model = Currency
    template_name = 'portfolio/currency/detail.html'
