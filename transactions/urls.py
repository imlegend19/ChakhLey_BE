from django.urls import path

from .views import TransactionListView, TransactionStaticVariableView
from .views import AcceptTransactionView

app_name = 'transaction'

urlpatterns = [
    path('', TransactionStaticVariableView.as_view(),
         name='get-static-transaction'),
    path('list/', TransactionListView.as_view(), name='list-transactions'),
    path('manager/', AcceptTransactionView.as_view(), name='create-transaction')
]