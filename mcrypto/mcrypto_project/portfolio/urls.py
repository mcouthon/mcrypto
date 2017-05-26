from django.conf.urls import url

from . import views


app_name = 'portfolio'
urlpatterns = [
    # ex: /portfolio/
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='index'
    ),
    # ex: /portfolio/cex/asset/
    url(
        regex=r'^(?P<pk>\w+)/asset/$',
        view=views.AssetDetail.as_view(),
        name='asset'
    ),
    # ex: /portfolio/5/holding/
    url(
        regex=r'^(?P<pk>[0-9]+)/holding/$',
        view=views.HoldingDetail.as_view(),
        name='holding'
    ),
    # ex: /portfolio/5/holding/edit/
    url(
        regex=r'^(?P<pk>[0-9]+)/holding/edit/$',
        view=views.HoldingUpdate.as_view(),
        name='edit_holding'
    ),
    # ex: /portfolio/usd/currency/
    url(
        regex=r'^(?P<pk>\w+)/currency/$',
        view=views.CurrencyDetail.as_view(),
        name='currency'
    ),
]
