from django.urls import path

from .views import *

app_name = "order"

urlpatterns = [
    path('list/', OrderListView.as_view(), name='order-list'),
    path('create/', CreateOrderView.as_view(), name='order-add'),
    path('<int:pk>/', RetrieveUpdateOrderView.as_view(), name='order-retrieve-update'),
    path('feedback/', ListCreateOrderFeedbackView.as_view(), name='order-feedback'),
]
