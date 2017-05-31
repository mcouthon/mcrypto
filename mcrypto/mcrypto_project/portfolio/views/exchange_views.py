from django.views.generic import DetailView, ListView

from ..models import ExchangeRate
from .mixins import LoginRequiredMixin


class ExchangeRateDetail(LoginRequiredMixin, DetailView):
    model = ExchangeRate
    template_name = 'portfolio/exchange/detail.html'


class ExchangeRateList(LoginRequiredMixin, ListView):
    model = ExchangeRate
    template_name = 'portfolio/exchange/exchange_rates.html'
    context_object_name = 'exchange_rate_list'
    paginate_by = 7

    def get_queryset(self):
        return ExchangeRate.objects.all().order_by('target__name')

    def get_context_data(self, **kwargs):
        context = super(ExchangeRateList, self).get_context_data(**kwargs)
        rate = ExchangeRate.objects.first()
        if rate:
            context['base'] = str(rate.base)
        return context
