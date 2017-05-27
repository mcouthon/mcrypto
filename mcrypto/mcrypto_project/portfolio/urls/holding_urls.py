from django.conf.urls import url

from ..views import holding_views


holding_url_patterns = [
    # ex: /portfolio/5/holding/
    url(
        regex=r'^(?P<pk>[0-9]+)/holding/$',
        view=holding_views.HoldingDetail.as_view(),
        name='holding'
    ),
    # ex: /portfolio/5/holding/edit/
    url(
        regex=r'^(?P<pk>[0-9]+)/holding/edit/$',
        view=holding_views.HoldingUpdate.as_view(),
        name='edit_holding'
    ),
    # ex: /portfolio/holding/add/
    url(
        regex=r'^holding/add/$',
        view=holding_views.HoldingCreate.as_view(),
        name='add_holding'
    )
]
