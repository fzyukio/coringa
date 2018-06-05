from django.conf.urls import url, include
from rest_framework_nested import routers
from users.api import UserViewSet
from ledgers.api import (AccountViewSet, PayeeViewSet, TransactionViewSet, LedgerViewSet,
                         NestedAccountViewSet, NestedPayeeViewSet, NestedTransactionViewSet)

app_name = "api"

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

router.register(r'ledgers', LedgerViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'payees', PayeeViewSet)
router.register(r'transactions', TransactionViewSet)

ledger_router = routers.NestedSimpleRouter(router, 'ledgers', lookup='ledger', trailing_slash=False)
ledger_router.register(r'accounts', NestedAccountViewSet, base_name='accounts')
ledger_router.register(r'payees', NestedPayeeViewSet, base_name='payees')
ledger_router.register(r'transactions', NestedTransactionViewSet, base_name='transactions')


urlpatterns = [
    url(r'^', include('authentication.urls')),
    url(r'^', include(router.urls)),
    url(r'^', include(ledger_router.urls)),
]
