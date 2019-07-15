import datetime

from django.db import models
from django.utils.text import gettext_lazy as _

from business.models import Business, DeliveryBoys

from business.models import Manager
from location.models import Area
from restaurant.models import Restaurant, ORDER_STATUS, PENDING, COMPLAINT, ORDER_FEEDBACK


class Order(models.Model):
    name = models.CharField(verbose_name=_("Buyer Name"), max_length=254)
    mobile = models.CharField(verbose_name=_("Mobile"), max_length=15)
    email = models.EmailField(verbose_name=_("Email"), max_length=255)
    business = models.ForeignKey(verbose_name=_("Business"), to=Business, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant, on_delete=models.PROTECT)
    preparation_time = models.DurationField(verbose_name=_('Preparation Time'), default=datetime.timedelta(minutes=40))
    status = models.CharField(verbose_name=_('Order Status'), max_length=5, choices=ORDER_STATUS, default=PENDING)
    order_date = models.DateTimeField(verbose_name=_('Order Create Date'), auto_now_add=True)

    @property
    def total(self):
        total = Delivery.objects.get(order=self.id).amount

        for so in self.suborder_set.all():
            total += so.sub_total

        return round(total, 2)

    @property
    def payment_done(self) -> bool:
        from django.db.models.aggregates import Sum

        payments = self.orderpayment_set.filter(is_credit=True).aggregate(
            Sum('amount'))['amount__sum']
        if payments:
            return payments == self.total
        else:
            return self.total == 0

    class Meta:
        ordering = ['-order_date', ]
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self) -> str:
        if self.name:
            return self.name
        elif self.id:
            return str(self.id)
        else:
            return "{status} Order".format(status=self.get_status_display())


class SubOrder(models.Model):

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


class Delivery(models.Model):
    order = models.OneToOneField(to=Order, on_delete=models.PROTECT, verbose_name=_('Order'))
    location = models.CharField(verbose_name=_("Location"), max_length=255, default='NIIT University')
    unit_no = models.CharField(verbose_name=_("Unit Number / Floor"), max_length=100)
    address_line_2 = models.CharField(verbose_name=_('Address Line 2'), max_length=255, null=True, blank=True)
    amount = models.DecimalField(verbose_name=_("Delivery Charge"), max_digits=10, decimal_places=2)

    @property
    def full_address(self):
        address = ''
        if self.unit_no:
            address += str(self.unit_no)
        if self.address_line_2:
            address += ", {}".format(self.address_line_2)
        address += ", {}".format(self.location)

        return address

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')

    def __str__(self):
        return self.order.name


class DeliveryBoysOrder(models.Model):
    deliver_boy = models.ForeignKey(verbose_name=_('Delivery Boy'), to=DeliveryBoys, on_delete=models.PROTECT)
    order = models.ForeignKey(verbose_name=_('Order'), to=Order, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Delivery Boys Order Data')
        verbose_name_plural = _('Delivery Boys Order Data')

    def __str__(self):
        return self.deliver_boy.employee.name


class OrderFeedback(models.Model):
    order_id = models.ForeignKey(verbose_name=_("Order Id"), to=Order, on_delete=models.PROTECT)
    type = models.CharField(verbose_name=_("Type"), choices=ORDER_FEEDBACK, max_length=100, default=COMPLAINT)
    description = models.TextField(verbose_name=_("Description"))
    mobile = models.CharField(verbose_name=_("User mobile"), max_length=255)

    class Meta:
        verbose_name = _("Order Feedback")
        verbose_name_plural = _("Order Feedback's")

    def __str__(self):
        return self.order_id
