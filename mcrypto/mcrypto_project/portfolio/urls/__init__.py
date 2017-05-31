from .api_urls import api_urlpatterns
from .user_urls import user_urlpatterns
from .asset_urls import asset_urlpatterns
from .generic_urls import generic_urlpatterns
from .holding_urls import holding_urlpatterns
from .currency_urls import currency_urlpatterns
from .exchange_urls import exchange_urlpatterns


app_name = 'portfolio'
urlpatterns = (
    holding_urlpatterns +
    asset_urlpatterns +
    currency_urlpatterns +
    user_urlpatterns +
    api_urlpatterns +
    exchange_urlpatterns +
    generic_urlpatterns
)
