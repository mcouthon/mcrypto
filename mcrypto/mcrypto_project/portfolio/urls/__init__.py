from django.conf.urls import url

from .. import views

from .user_urls import user_urlpatterns
from .asset_urls import asset_urlpatterns
from .holding_urls import holding_urlpatterns
from .currency_urls import currency_urlpatterns


app_name = 'portfolio'
urlpatterns = (
    holding_urlpatterns +
    asset_urlpatterns +
    currency_urlpatterns +
    user_urlpatterns +
    [
        # ex: /portfolio/
        url(
            regex=r'^$',
            view=views.IndexView.as_view(),
            name='index'
        )
    ]
)
