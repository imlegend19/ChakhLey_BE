from django.db import models
from django.utils.text import gettext_lazy as _
from drf_user.models import User

from ChakhLe_BE.variables import BUSINESS


class Business(models.Model):
    from location.models import City

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    type = models.CharField(verbose_name=_('Type'), choices=BUSINESS, max_length=255)
    city = models.ForeignKey(verbose_name=_('City'), to=City, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Business')
        verbose_name_plural = _('Businesses')


class DeliveryBoys(models.Model):
    from employee.models import Employee

    salary = models.DecimalField(verbose_name=_('Salary'), max_digits=10, decimal_places=2, default=0)
    employee = models.ForeignKey(verbose_name=_('Employee Id'), to=Employee, on_delete=models.PROTECT)
    is_active = models.BooleanField(verbose_name=_('Is Active ?'), default=True)
    start_time = models.TimeField(verbose_name=_('Start Time'), max_length=255)
    end_time = models.TimeField(verbose_name=_('End Time'), max_length=255)
    joined_on = models.DateField(verbose_name=_("Join Date"), null=True,
                                 blank=True)
    left_on = models.DateField(verbose_name=_("Leave Date"), null=True,
                               blank=True)

    class Meta:
        verbose_name = _('Delivery Boy')
        verbose_name_plural = _('Delivery Boys')

    def __str__(self):
        return self.employee.name


class Manager(models.Model):
    from employee.models import Employee

    employee = models.ForeignKey(verbose_name=_('Employee Id'), to=Employee, on_delete=models.PROTECT)
    business = models.ForeignKey(verbose_name=_('Business'), to=Business, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Manager')
        verbose_name_plural = _('Managers')

    def __str__(self):
        return self.employee.name
