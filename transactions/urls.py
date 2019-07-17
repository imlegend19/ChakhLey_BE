from django.urls import path

from .views import *
from .views import AcceptTransactionView

app_name = 'transaction'

urlpatterns = [
    path('', TransactionStaticVariableView.as_view(),
         name='get-static-transaction'),
    path('list/', TransactionListView.as_view(), name='list-transactions'),
    path('<int:pk>/', TransactionDestroyView.as_view(), name='delete_transaction'),
    path('create/', AcceptTransactionView.as_view(), name='create-transaction')
]
