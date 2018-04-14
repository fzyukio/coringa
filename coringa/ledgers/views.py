from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView
from common.mixins import ShowOnlyUserObjectsMixin, CreateFormWithUserMixin
from ledgers.models import Ledger


class LedgerCreateView(LoginRequiredMixin, CreateFormWithUserMixin, CreateView):
    model = Ledger
    fields = ['name']

    def get_success_url(self):
        return reverse('ledgers:list')


class LedgerUpdateView(LoginRequiredMixin, ShowOnlyUserObjectsMixin, UpdateView):
    model = Ledger
    fields = ['name']


class LedgerListView(LoginRequiredMixin, ShowOnlyUserObjectsMixin, ListView):
    model = Ledger


class LedgerDetailView(LoginRequiredMixin, ShowOnlyUserObjectsMixin, DetailView):
    model = Ledger
    # These next two lines tell the view to index lookups by username
    slug_field = 'id'
    slug_url_kwarg = 'ledger'
