from django.views.generic import ListView

from ..models import Currency

# Importing here to make it easier to import from `views`
from .holding import HoldingDetail, HoldingUpdate   # NOQA
from .currency import CurrencyDetail                # NOQA
from .asset import AssetDetail                      # NOQA


class IndexView(ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'currency_list'

    def get_queryset(self):
        return Currency.objects.all()
