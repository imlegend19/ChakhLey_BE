import datetime
from django.db import models
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel
from ChakhLe_BE.variables import *


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
        from order.models import Order

        total = 0
        for i in Order.objects.filter(restaurant=self.id):
            total += i.total - float(i.delivery.amount) - float(i.packaging_charge)

        return total

    @property
    def income_today(self):
        from order.models import Order

        total = 0
        for i in Order.objects.filter(restaurant=self.id,
                                      order_date__gte=datetime.datetime.now().replace(hour=0, minute=0, second=0)):
            total += i.total - float(i.delivery.amount) - float(i.packaging_charge)

        return total

    @property
    def income_month(self):
        from django.db import connection

        cursor = connection.cursor()
        cursor.execute('''select sum(price * quantity) from product_product inner join
                   (select * from order_suborder where order_id in (select id from order_order 
                   where month(order_date) = month(current_date))) as os on product_product.id = os.item_id''')

        return cursor.fetchone()[0]

    @property
    def total_orders(self):
        from order.models import Order
        return Order.objects.filter(restaurant=self.id) \
            .count()

    @property
    def orders_month(self):
        from django.db import connection

        cursor = connection.cursor()
        cursor.execute('''select count(*) from order_order where month(order_date) = month(current_date)''')

        return cursor.fetchone()[0]

    @property
    def orders_today(self):
        from django.db import connection

        cursor = connection.cursor()
        cursor.execute('''select count(*) from order_order where day(order_date) = day(current_date)''')

        return cursor.fetchone()[0]

    @property
    def most_liked_product(self):
        from product.models import Product
        from order.models import SubOrder

        product_count = {}
        for i in SubOrder.objects.filter(order__restaurant=self.id):
            if i.item in product_count:
                val = product_count[i.item] + i.quantity
                product_count[i.item] = val
            else:
                product_count[i.item] = i.quantity

        sorted_x = sorted(product_count.items(), key=lambda kv: kv[1], reverse=True)

        try:
            i = sorted_x[0][0]
            item = {'id': i.id, 'name': i.name, 'category': i.category.id, 'is_veg': i.is_veg, 'price': i.price,
                    'discount': i.discount, 'inflation': i.inflation, 'active': i.active,
                    'image_url': i.image_url if not None else '',
                    'description': i.description if not None else '', 'restaurant': i.restaurant,
                    'recommended_product': i.recommended_product, 'display_price': i.display_price,
                    'total_sale': sorted_x[0][1]}

            x = 123
            return item
        except IndexError as e:
            print(e)

    @property
    def top_10_products(self):
        from product.models import Product
        from order.models import SubOrder

        product_count = {}
        for i in SubOrder.objects.filter(order__restaurant=self.id):
            if i.item in product_count:
                val = product_count[i.item] + i.quantity
                product_count[i.item] = val
            else:
                product_count[i.item] = i.quantity

        sorted_x = sorted(product_count.items(), key=lambda kv: kv[1], reverse=True)

        products = []
        if len(sorted_x) > 10:
            for x in range(10):
                i = sorted_x[x][0]
                item = {'id': i.id, 'name': i.name, 'category': i.category.id, 'is_veg': i.is_veg, 'price': i.price,
                        'discount': i.discount, 'inflation': i.inflation, 'active': i.active, 'image_url': i.image_url,
                        'description': i.description, 'restaurant': i.restaurant,
                        'recommended_product': i.recommended_product, 'display_price': i.display_price,
                        'total_sale': sorted_x[i][1]}

                products.append(item)
        else:
            for x in range(len(sorted_x)):
                i = sorted_x[x][0]
                item = {'id': i.id, 'name': i.name, 'category': i.category.id, 'is_veg': i.is_veg, 'price': i.price,
                        'discount': i.discount, 'inflation': i.inflation, 'active': i.active, 'image_url': i.image_url,
                        'description': i.description, 'restaurant': i.restaurant,
                        'recommended_product': i.recommended_product, 'display_price': i.display_price,
                        'total_sale': sorted_x[x][1]}

                products.append(item)

        return products

    @property
    def amount_after_commission(self):
        from django.db import connection

        cursor = connection.cursor()
        cursor.execute('''select sum(price * quantity) from product_product inner join
           (select * from order_suborder where order_id in (select id from order_order 
           where month(order_date) = month(current_date))) as os on product_product.id = os.item_id''')

        income_month = cursor.fetchone()[0]
        print(self.commission)
        return income_month - (income_month * self.commission) / 100

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
