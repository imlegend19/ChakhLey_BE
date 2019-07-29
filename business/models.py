from django.db import models
from django.utils.text import gettext_lazy as _
from drf_user.models import User

from ChakhLe_BE.variables import BUSINESS


class Business(models.Model):
    from location.models import City

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    type = models.CharField(verbose_name=_('Type'), choices=BUSINESS, max_length=255)
    city = models.ForeignKey(verbose_name=_('City'), to=City, on_delete=models.PROTECT)
    latitude = models.DecimalField(verbose_name=_("Latitude"), max_digits=10, decimal_places=8, default=27.988889)
    longitude = models.DecimalField(verbose_name=_("Longitude"), max_digits=11, decimal_places=8, default=76.388333)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Business')
        verbose_name_plural = _('Businesses')
