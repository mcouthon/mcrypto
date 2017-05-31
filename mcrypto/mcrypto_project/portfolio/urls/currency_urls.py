from django.conf.urls import url

from ..views import currency_views


currency_urlpatterns = [
    # ex: /portfolio/5/currency/
    url(
        regex=r'^(?P<pk>\w+)/currency/$',
        view=currency_views.CurrencyDetail.as_view(),
        name='currency'
    ),
]
