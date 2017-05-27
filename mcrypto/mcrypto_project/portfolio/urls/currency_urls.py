from django.conf.urls import url

from .. import views

# ex: /portfolio/usd/currency/
currency_url_patterns = [
    url(
        regex=r'^(?P<pk>\w+)/currency/$',
        view=views.CurrencyDetail.as_view(),
        name='currency'
    ),
]
