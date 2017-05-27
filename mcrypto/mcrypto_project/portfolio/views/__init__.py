from django.views.generic import ListView

from ..models import Currency

# Importing here to make it easier to import from `views`
from .holding_views import (                # NOQA
    HoldingDetail,
    HoldingUpdate,
    HoldingCreate
)
from .currency_views import CurrencyDetail  # NOQA
from .asset_views import (                  # NOQA
    AssetDetail,
    AssetCreate,
    AssetUpdate,
    AssetView
)


class IndexView(ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'currency_list'

    def get_queryset(self):
        return Currency.objects.all()
