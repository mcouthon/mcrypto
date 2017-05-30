from django.views.generic import ListView


from ..models import Currency
from .mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'currency_list'
    paginate_by = 10

    def get_queryset(self):
        return Currency.objects.all()
