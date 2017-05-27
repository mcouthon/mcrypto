from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView

from ..models import Asset


class AssetDetail(DetailView):
    model = Asset
    template_name = 'portfolio/asset.html'


class AssetUpdate(UpdateView):
    model = Asset
    template_name_suffix = '_edit'
    fields = ['name', 'description']


class AssetCreate(CreateView):
    model = Asset
    template_name_suffix = '_edit'
    fields = ['name', 'description']


class AssetView(ListView):
    template_name = 'portfolio/assets.html'
    context_object_name = 'asset_list'

    def get_queryset(self):
        return Asset.objects.all()
