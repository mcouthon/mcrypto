from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView

from ..models import Holding
from .mixins import LoginRequiredMixin


class HoldingDetail(LoginRequiredMixin, DetailView):
    model = Holding
    template_name = 'portfolio/holding/detail.html'


class HoldingUpdate(LoginRequiredMixin, UpdateView):
    model = Holding
    template_name = 'portfolio/holding/holding_edit.html'
    fields = ['asset', 'coin', 'amount']


class HoldingCreate(LoginRequiredMixin, CreateView):
    model = Holding
    template_name = 'portfolio/holding/holding_edit.html'
    fields = ['asset', 'coin', 'amount']
