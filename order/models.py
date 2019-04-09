import datetime

from django.db import models
from django.utils.text import gettext_lazy as _
from drfaddons.models import CreateUpdateModel

from business.models import Business, DeliveryBoys

from business.models import Manager
from location.models import Area
from restaurant.models import Restaurant, ORDER_STATUS, PENDING


class Order(CreateUpdateModel):
    name = models.CharField(verbose_name=_("Buyer Name"), max_length=254)
    mobile = models.CharField(verbose_name=_("Mobile"), max_length=15)
    email = models.EmailField(verbose_name=_("Email"), max_length=255)
    business = models.ForeignKey(verbose_name=_("Business"), to=Business, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant, on_delete=models.PROTECT)
    preparation_time = models.DurationField(verbose_name=_('Preparation Time'), default=datetime.timedelta(minutes=40))
    status = models.CharField(verbose_name=_('Order Status'), max_length=5, choices=ORDER_STATUS, default=PENDING)
    managed_by = models.ForeignKey(verbose_name=_('Managed By'), to=Manager, on_delete=models.PROTECT)
    order_date = models.DateTimeField(_('Order Create Date'), max_length=255)

    @property
    def total(self):
        total = 0

        for so in self.suborder_set.all():
            total += so.sub_total

        return round(total, 2)

    class Meta:
        ordering = ['-create_date', ]
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.name


class SubOrder(CreateUpdateModel):

    from product.models import Product

    order = models.ForeignKey(verbose_name=_('Order'), to=Order, on_delete=models.PROTECT)
    item = models.ForeignKey(verbose_name=_('Product'), to=Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))

    @property
    def product(self):
        return self.item

    @property
    def sub_total(self):
        return self.item.price * self.quantity

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = _('Sub Order')
        verbose_name_plural = _('Sub Orders')


class Delivery(CreateUpdateModel):
    order = models.OneToOneField(to=Order, on_delete=models.PROTECT, verbose_name=_('Order'))
    amount = models.DecimalField(verbose_name=_('Delivery Amount'), default=20, max_digits=10, decimal_places=2)
    area = models.ForeignKey(to=Area, on_delete=models.PROTECT, verbose_name=_('Area'))
    unit_no = models.CharField(verbose_name=_("Unit Number / Floor"), max_length=100)
    address_line_2 = models.CharField(verbose_name=_('Address Line 2'), max_length=255, null=True, blank=True)

    @property
    def full_address(self):
        address = str(self.unit_no)
        if self.address_line_2:
            address += ", {}".format(self.address_line_2)
        address += ", {}".format(self.area.name)
        address += ", {}".format(self.area.city.name)
        address += ", {}".format(self.area.city.state.name)
        address += ", {}".format(self.area.city.state.country.name)
        address += ", {}".format(self.area.pincode)

        return address

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')

    def __str__(self):
        return self.order.name


class DeliveryBoysOrder(CreateUpdateModel):
    deliver_boy = models.ForeignKey(verbose_name=_('Delivery Boy'), to=DeliveryBoys, on_delete=models.PROTECT)
    order = models.ForeignKey(verbose_name=_('Order'), to=Order, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Delivery Boys Order Data')
        verbose_name_plural = _('Delivery Boys Order Data')

    def __str__(self):
        return self.deliver_boy.user.name
