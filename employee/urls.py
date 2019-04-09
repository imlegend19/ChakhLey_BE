from django.urls import path

from .views import EmployeeView

app_name = "employee"

urlpatterns = [
    path('', EmployeeView.as_view(), name="employee_list"),
]
