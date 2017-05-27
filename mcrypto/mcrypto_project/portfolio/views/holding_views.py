from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView

from ..models import Holding


class HoldingDetail(DetailView):
    model = Holding
    template_name = 'portfolio/holding.html'


class HoldingUpdate(UpdateView):
    model = Holding
    template_name_suffix = '_edit'
    fields = ['asset', 'coin', 'amount']


class HoldingCreate(CreateView):
    model = Holding
    template_name_suffix = '_edit'
    fields = ['asset', 'coin', 'amount']
