from django.conf.urls import url

from ..views import asset_views


asset_urlpatterns = [
    # ex: /portfolio/assets
    url(
        regex=r'^assets/$',
        view=asset_views.AssetView.as_view(),
        name='assets'
    ),
    # ex: /portfolio/4/asset/
    url(
        regex=r'^(?P<pk>\w+)/asset/$',
        view=asset_views.AssetDetail.as_view(),
        name='asset'
    ),
    # ex: /portfolio/5/asset/edit/
    url(
        regex=r'^(?P<pk>[0-9]+)/asset/edit/$',
        view=asset_views.AssetUpdate.as_view(),
        name='edit_asset'
    ),
    # ex: /portfolio/asset/add/
    url(
        regex=r'^asset/add/$',
        view=asset_views.AssetCreate.as_view(),
        name='add_asset'
    )
]
