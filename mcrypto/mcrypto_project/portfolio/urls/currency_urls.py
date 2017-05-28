from django.conf.urls import url

from .. import views

currency_urlpatterns = [
    # ex: /portfolio/usd/currency/
    url(
        regex=r'^(?P<pk>\w+)/currency/$',
        view=views.CurrencyDetail.as_view(),
        name='currency'
    ),
]
