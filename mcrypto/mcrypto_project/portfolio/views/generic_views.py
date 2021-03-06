from django.views.generic import TemplateView

from .mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio/index.html'
