from django.conf.urls import url

from ..views import generic_views


generic_urlpatterns = [
    # ex: /portfolio/
    url(
        regex=r'^$',
        view=generic_views.IndexView.as_view(),
        name='index'
    )
]
