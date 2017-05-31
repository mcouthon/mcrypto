from django.conf.urls import url

from ..views import api_views


api_urlpatterns = [
    # ex: /portfolio/api/currencies
    url(
        regex=r'^api/currencies/$',
        view=api_views.CurrencyUpdateView.as_view(),
        name='update_currencies'
    ),
    # ex: /portfolio/api/exchange
    url(
        regex=r'^api/exchange/$',
        view=api_views.ExchangeUpdateView.as_view(),
        name='update_exchange_rate'
    ),
    # ex: /portfolio/api/crypto_exchange
    url(
        regex=r'^api/crypto_exchange/$',
        view=api_views.CryptoExchangeUpdateView.as_view(),
        name='update_crypto_exchange_rate'
    ),
]
