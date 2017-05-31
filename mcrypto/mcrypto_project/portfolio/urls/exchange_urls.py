from django.conf.urls import url

from ..views import exchange_views


exchange_urlpatterns = [
    # ex: /portfolio/6/exchange/
    url(
        regex=r'^(?P<pk>\w+)/exchange/$',
        view=exchange_views.ExchangeRateDetail.as_view(),
        name='exchange_rate'
    ),
    # ex: /portfolio/exchange_rates
    url(
        regex=r'^exchange_rates/$',
        view=exchange_views.ExchangeRateList.as_view(),
        name='exchange_rates'
    ),
]
