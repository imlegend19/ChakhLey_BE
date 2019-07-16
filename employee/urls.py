from django.urls import path

from .views import *

app_name = "employee"

urlpatterns = [
    path('', EmployeeView.as_view(), name="employee-list"),
    path('<int:pk>/', RetrieveUpdateEmployeeView.as_view(), name='employee-retrieve-update'),
    path('document/', EmployeeDocumentView.as_view(), name="employee-document")
]
