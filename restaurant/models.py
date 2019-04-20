from django.db import models
from django.utils.text import gettext_lazy as _
import datetime

from drfaddons.models import CreateUpdateModel

from ChakhLe_BE.variables import *


class Restaurant(CreateUpdateModel):
    from location.models import Area
    from business.models import Business

    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)
    area = models.ForeignKey(verbose_name=_('Area'), to=Area, on_delete=models.PROTECT)
    unit = models.CharField(verbose_name=_("Unit No"), max_length=255,
                            null=True, blank=True)
    business = models.ForeignKey(verbose_name=_('Business'), to=Business, on_delete=models.PROTECT, default=1)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=255)
    email = models.EmailField(verbose_name=_('Email'), max_length=255, blank=True, null=True)
    website = models.URLField(verbose_name=_('Website / Online Listing Link'), max_length=255, blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("Is Active?"),
                                    default=True)
    cost_for_two = models.CharField(verbose_name=_('Cost For Two'), choices=COST_FOR_TWO, max_length=255)
    cuisine = models.CharField(verbose_name=_('Type of Cuisine'), choices=CUISINES, max_length=255)
    establishment = models.CharField(verbose_name=_('Establishment'), choices=ESTABLISHMENTS, max_length=255)
    delivery_time = models.IntegerField(verbose_name=_('Delivery Time'), default=40)
    is_veg = models.BooleanField(verbose_name=_('Is Veg?'), default=True)
    commission = models.IntegerField(verbose_name=_("Commission"), default=10)
    open_from = models.TimeField(verbose_name=_("Open From"), default=datetime.time(hour=11, minute=30))
    open_till = models.TimeField(verbose_name=_("Open Till"), default=datetime.time(hour=23))

    def __str__(self):
        return self.name

    @property
    def category_count(self):
        from product.models import Category

        return Category.objects.all().filter(restaurant_id=self.id).count()

    @property
    def open(self):
        import pytz

        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.datetime.now().astimezone(tz).time()

        if self.open_from <= now <= self.open_till:
            return True
        else:
            return False

    @property
    def full_address(self):
        address = ''

        if self.unit:
            address += self.unit

        if self.area:
            address += ', ' + self.area.name

        if self.area.city:
            address += ', ' + self.area.city.name + ', ' + self.area.city.state.name

        if self.area.city.state.country:
            address += ', ' + self.area.city.state.country.name

        if self.area.pincode:
            address += ', ' + self.area.pincode

        return address

    class Meta:
        ordering = ['-commission']
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class RestaurantImage(CreateUpdateModel):

    from .utils import outlet_image_upload

    name = models.CharField(verbose_name=_('Image Name'), choices=IMAGE_TYPES, max_length=255, default=RESTAURANT)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), on_delete=models.PROTECT, to=Restaurant)
    image = models.ImageField(verbose_name=_('Select Image'), upload_to=outlet_image_upload)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurant Image'
        verbose_name_plural = 'Restaurant Images'
