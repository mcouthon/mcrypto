from django.conf.urls import url

from .. import views

from .asset_urls import asset_url_patterns
from .holding_urls import holding_url_patterns
from .currency_urls import currency_url_patterns


app_name = 'portfolio'
urlpatterns = (
    holding_url_patterns +
    asset_url_patterns +
    currency_url_patterns +
    [
        # ex: /portfolio/
        url(
            regex=r'^$',
            view=views.IndexView.as_view(),
            name='index'
        )
    ]
)
