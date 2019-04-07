from django.db import models
from django.utils.text import gettext_lazy as _

from ChakhLe_BE.variables import *
from location.models import City, Country, State, Area


class Restaurant(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)
    pincode = models.CharField(verbose_name=_('ZIP (Primary Location'), max_length=6)
    country = models.ForeignKey(verbose_name=_('Country'), to=Country, on_delete=models.PROTECT)
    state = models.ForeignKey(verbose_name=_('State'), to=State, on_delete=models.PROTECT)
    city = models.ForeignKey(verbose_name=_('City'), to=City, on_delete=models.PROTECT)
    area = models.ForeignKey(verbose_name=_('Area'), to=Area, on_delete=models.PROTECT)
    unit = models.CharField(verbose_name=_("Unit No"), max_length=255,
                            null=True, blank=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=255)
    email = models.EmailField(verbose_name=_('Email'), max_length=255)
    website = models.URLField(verbose_name=_('Website / Online Listing Link'), max_length=255, blank=True)
    is_active = models.BooleanField(verbose_name=_("Is Active?"),
                                    default=True)
    cost_for_two = models.CharField(verbose_name=_('Cost For Two'), choices=COST_FOR_TWO, max_length=255,
                                    default=BASIC_COST)
    cuisine = models.CharField(verbose_name=_('Type of Cuisine'), choices=CUISINES, max_length=255)
    establishment = models.CharField(verbose_name=_('Establishment'), choices=ESTABLISHMENTS, max_length=255)
    delivery_time = models.DecimalField(verbose_name=_('Delivery Time'), max_digits=10, decimal_places=2)
    is_veg = models.BooleanField(verbose_name=_('Is Veg?'), default=True)

    def __str__(self):
        return self.name

    @property
    def full_address(self):
        address = ''

        if self.unit:
            address += self.unit

        if self.area:
            address += ', ' + self.area.name

        if self.city:
            address += ', ' + self.city.name + ', ' + self.city.state.name

        if self.country:
            address += ', ' + self.country.name

        if self.pincode:
            address += ', ' + self.pincode

        return address

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class RestaurantImage(models.Model):

    from .utils import outlet_image_upload

    name = models.CharField(verbose_name=_('Image Name'), choices=IMAGE_TYPES, max_length=255, default=RESTAURANT)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), on_delete=models.PROTECT, to=Restaurant)
    image = models.ImageField(upload_to=outlet_image_upload)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurant Image'
        verbose_name_plural = 'Restaurant Images'
