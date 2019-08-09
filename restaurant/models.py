import datetime

from django.forms import model_to_dict
from product.models import Product
from order.models import Order, SubOrder
from django.db import models
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel
from django.db.models import Sum, Count
from ChakhLe_BE.variables import *


def get_product_count(restaurant_id):
    product_count = {}
    for i in SubOrder.objects.all().filter(order__restaurant=restaurant_id):
        if i.item in product_count:
            val = product_count[i.item] + i.quantity
            product_count[i.item] = val
        else:
            product_count[i.item] = i.quantity

    sorted_x = sorted(product_count.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_x


class Restaurant(CreateUpdateModel):
    from location.models import Area
    from business.models import Business

    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)
    area = models.ForeignKey(verbose_name=_('Area'), to=Area, on_delete=models.PROTECT)
    unit = models.CharField(verbose_name=_("Unit No"), max_length=255, null=True, blank=True)
    business = models.ForeignKey(verbose_name=_('Business'), to=Business, on_delete=models.PROTECT, default=1)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=255)
    email = models.EmailField(verbose_name=_('Email'), max_length=255, blank=True, null=True)
    website = models.URLField(verbose_name=_('Website / Online Listing Link'), max_length=255, blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("Is Active?"), default=True)
    cost_for_two = models.CharField(verbose_name=_('Cost For Two'), choices=COST_FOR_TWO, max_length=255)
    establishment = models.CharField(verbose_name=_('Establishment'), choices=ESTABLISHMENTS, max_length=255)
    delivery_time = models.IntegerField(verbose_name=_('Delivery Time'), default=40)
    is_veg = models.BooleanField(verbose_name=_('Is Veg?'), default=True)
    commission = models.IntegerField(verbose_name=_("Commission"), default=10)
    open_from = models.TimeField(verbose_name=_("Open From"), default=datetime.time(hour=11, minute=30))
    open_till = models.TimeField(verbose_name=_("Open Till"), default=datetime.time(hour=23))
    latitude = models.DecimalField(verbose_name=_("Latitude"), max_digits=10, decimal_places=8, default=27.978237)
    longitude = models.DecimalField(verbose_name=_("Longitude"), max_digits=11, decimal_places=8, default=76.4000549)
    discount = models.IntegerField(verbose_name=_("Discount"), default=0)
    packaging_charge = models.DecimalField(verbose_name=_("Packaging Charge"), max_digits=10, decimal_places=2,
                                           default=0)
    gst = models.BooleanField(verbose_name=_("GST Charge"), default=False)

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
            if self.is_active:
                return True
            else:
                return False
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

    @property
    def cuisine(self):
        from ChakhLe_BE.variables import CUISINES_DICT
        cuisine = []

        for i in RestaurantCuisine.objects.filter(restaurant=self.id):
            cuisine.append(CUISINES_DICT[i.cuisine])

        return cuisine

    @property
    def images(self):
        images = []

        for i in RestaurantImage.objects.filter(restaurant=self.id):
            file = URL
            image_path = i.image.file.name
            file += image_path[image_path.find('images/'):]
            images.append(file)

        return images

    @property
    def total_income(self):
        return Order.objects.all().filter(restaurant=self.id)\
            .aggregate(Sum('total'))

    @property
    def total_orders(self):
        return Order.objects.all().filter(restaurant=self.id)\
            .count()

    @property
    def orders_today(self):
        return Order.objects.all().filter(restaurant=self.id, order_date=datetime.datetime.today())\
            .count()

    @property
    def income_today(self):
        return Order.objects.all().filter(restaurant=self.id, order_date=datetime.datetime.today())\
            .aggregate(Sum('total'))

    @property
    def most_liked_product(self):
        sorted_x = get_product_count(self.id)
        item = model_to_dict(Product.objects.all().get(id=sorted_x[0][0]))
        item['total_sale'] = sorted_x[0][1]

        return item

    @property
    def top_10_products(self):
        sorted_x = get_product_count(self.id)
        products = []
        if len(sorted_x) > 10:
            for i in range(10):
                item = model_to_dict(Product.objects.all().get(id=sorted_x[i][0]))
                item['total_sale'] = sorted_x[i][1]

                products.append(item)
        else:
            for i in range(len(sorted_x)):
                item = model_to_dict(Product.objects.all().get(id=sorted_x[i][0]))
                item['total_sale'] = sorted_x[i][1]

                products.append(item)

        return products

    @property
    def per_day_average(self):
        avg = Order.objects.all().filter(restaurant=self.id)\
            .extra({'weekday': "dayofweek(order_date)"})\
            .values('weekday')\
            .annotate(Count('id'))

        return avg

    class Meta:
        ordering = ['-commission']
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class RestaurantImage(CreateUpdateModel):
    image_type = models.CharField(verbose_name=_('Image Type'), choices=IMAGE_TYPES, max_length=255, default=RESTAURANT)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), on_delete=models.PROTECT, to=Restaurant)
    image = models.ImageField(verbose_name=_('Select Image'), upload_to='media/')

    def __str__(self):
        return self.restaurant.name + " - " + IMAGE_TYPES_DICT[self.image_type]

    class Meta:
        verbose_name = 'Restaurant Image'
        verbose_name_plural = 'Restaurant Images'


class RestaurantCuisine(models.Model):
    restaurant = models.ForeignKey(verbose_name=_("Restaurant"), to=Restaurant, on_delete=models.PROTECT)
    cuisine = models.CharField(verbose_name=_("Cuisine"), choices=CUISINES, max_length=255)

    def __str__(self):
        return self.restaurant.name

    class Meta:
        verbose_name = _("Restaurant Cuisine")
        verbose_name_plural = _("Restaurant Cuisines")
