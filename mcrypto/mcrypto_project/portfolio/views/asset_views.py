from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView

from ..models import Asset


class AssetDetail(DetailView):
    model = Asset
    template_name = 'portfolio/asset/detail.html'


class AssetUpdate(UpdateView):
    model = Asset
    template_name = 'portfolio/asset/asset_edit.html'
    fields = ['name', 'description']


class AssetCreate(CreateView):
    model = Asset
    template_name = 'portfolio/asset/asset_edit.html'
    fields = ['name', 'description']


class AssetView(ListView):
    template_name = 'portfolio/asset/assets.html'
    context_object_name = 'asset_list'

    def get_queryset(self):
        return Asset.objects.all()
