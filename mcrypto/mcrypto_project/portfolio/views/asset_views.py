from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView

from ..models import Asset
from .mixins import LoginRequiredMixin


class AssetDetail(LoginRequiredMixin, DetailView):
    model = Asset
    template_name = 'portfolio/asset/detail.html'


class AssetUpdate(LoginRequiredMixin, UpdateView):
    model = Asset
    template_name = 'portfolio/asset/asset_edit.html'
    fields = ['name', 'description']


class AssetCreate(LoginRequiredMixin, CreateView):
    model = Asset
    template_name = 'portfolio/asset/asset_edit.html'
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('portfolio:asset', kwargs={'pk': self.object.pk})


class AssetView(LoginRequiredMixin, ListView):
    model = Asset
    template_name = 'portfolio/asset/assets.html'
    context_object_name = 'asset_list'

    def get_queryset(self):
        return Asset.objects.all()
