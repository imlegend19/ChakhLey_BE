from django.db import models
from django.utils.text import gettext_lazy as _


class Country(models.Model):
    """
    Represents all countries

    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


class State(models.Model):
    """
    Represents all states

    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    name = models.CharField(verbose_name=_('State'), max_length=255, unique=True)
    country = models.ForeignKey(verbose_name=_('Country'), to=Country, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')


class City(models.Model):
    """
    Represents all cities

    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    name = models.CharField(verbose_name=_('City'), max_length=255, unique=True)
    state = models.ForeignKey(verbose_name=_('State'), to=State, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class Area(models.Model):
    """
    Represents all areas

    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    name = models.CharField(verbose_name=_('Area'), max_length=255, unique=True)
    city = models.ForeignKey(verbose_name=_('City'), to=City, on_delete=models.PROTECT)
    pincode = models.CharField(verbose_name=_('Pincode'), max_length=6, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Area')
        verbose_name_plural = _('Areas')
