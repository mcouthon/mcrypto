from django.views.generic import DetailView

from ..models import Asset


class AssetDetail(DetailView):
    model = Asset
    template_name = 'portfolio/asset.html'
