from django.conf.urls import url

from . import views

app_name = "ledgers"
urlpatterns = [
    url(
        regex=r'^$',
        view=views.LedgerListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~create/$',
        view=views.LedgerCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<ledger>[0-9a-f-]+)/$',
        view=views.LedgerDetailView.as_view(),
        name='detail'
    ),
]
