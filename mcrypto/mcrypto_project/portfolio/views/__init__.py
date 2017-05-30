# Importing here to allow importing from `portfolio.views`

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
from .generic_views import IndexView        # NOQA
