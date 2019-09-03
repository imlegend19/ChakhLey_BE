import datetime

from django.db import models
from django.utils.text import gettext_lazy as _
from business.models import Business
from employee.models import Employee
from location.models import Area
from ChakhLey_BE.variables import ORDER_STATUS, NEW, COMPLAINT, ORDER_FEEDBACK


class Order(models.Model):
    """
    Represents all orders in the system.

    @author: Mahen Gandhi (https://github.com/imlegend19)
    @author: Yugandhar Desai (https://github.com/yugi1729)
    """
    from restaurant.models import Restaurant
    from promocode.models import Offer, UserPromoCode

    name = models.CharField(verbose_name=_("Buyer Name"), max_length=254)
    mobile = models.CharField(verbose_name=_("Mobile"), max_length=15)
    email = models.EmailField(verbose_name=_("Email"), max_length=255, null=True, blank=True)
    business = models.ForeignKey(verbose_name=_("Business"), to=Business, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant, on_delete=models.PROTECT)
    preparation_time = models.DurationField(verbose_name=_('Preparation Time'), default=datetime.timedelta(minutes=40))
    status = models.CharField(verbose_name=_('Order Status'), max_length=5, choices=ORDER_STATUS, default=NEW)
    order_date = models.DateTimeField(verbose_name=_('Order Create Date'), auto_now_add=True)
    delivery_boy = models.ForeignKey(verbose_name=_("Delivery Boy"), to=Employee, on_delete=models.PROTECT, null=True,
                                     blank=True)
    offer = models.ForeignKey(verbose_name=_('Offer'), to=Offer, on_delete=models.PROTECT,
                              null=True, blank=True)
    user_promo_code = models.ForeignKey(verbose_name=_('User Promo Code'), to=UserPromoCode, on_delete=models.PROTECT,
                                        null=True, blank=True)

    @property
    def packaging_charge(self) -> float:
        """
        @return: Restaurant default packaging charge rounded off 2 decimal places
        """
        packaging_charge = float(self.restaurant.packaging_charge)
        return round(packaging_charge, 2)

    @property
    def has_delivery_boy(self) -> bool:
        """
        @return: delivery boy allotted ?
        """
        if self.delivery_boy:
            return True
        else:
            return False

    @property
    def total(self) -> float:
        """
        Total amount for the order

        @return: float --> Delivery Charge (amount) + Packaging charge + Suborder items charge
        """
        total = float(Delivery.objects.get(order=self.id).amount) + self.packaging_charge

        for so in self.suborder_set.all():
            total += so.sub_total

        return round(total, 2)

    @property
    def payment_done(self) -> bool:
        """
        Payment done for order? Refers OrderPayment model to check whether total amount exists

        @return: bool
        """
        from django.db.models.aggregates import Sum
        from transactions.models import OrderPayment

        payments = OrderPayment.objects.filter(is_credit=True, order=self.id).aggregate(Sum('amount'))['amount__sum']
        if payments:
            return payments >= self.total
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
    """
    Represent all suborder models in the system.

    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    from product.models import Product

    order = models.ForeignKey(verbose_name=_('Order'), to=Order, on_delete=models.PROTECT)
    item = models.ForeignKey(verbose_name=_('Product'), to=Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))

    @property
    def product(self):
        """
        @return: Item foreign key id
        """
        return self.item

    @property
    def sub_total(self):
        """
        @return: Total price of an item in the suborder
        """
        return self.item.display_price * self.quantity

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = _('Sub Order')
        verbose_name_plural = _('Sub Orders')


class Delivery(models.Model):
    """
    Delivery model to save the delivery address and fee in the system.

    @requires order, location, amount
    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    order = models.OneToOneField(to=Order, on_delete=models.PROTECT, verbose_name=_('Order'))
    location = models.CharField(verbose_name=_("Location"), max_length=255, default='NIIT University')
    unit_no = models.CharField(verbose_name=_("Unit Number / Floor"), max_length=100)
    address_line_2 = models.CharField(verbose_name=_('Address Line 2'), max_length=255, null=True, blank=True)
    amount = models.DecimalField(verbose_name=_("Delivery Charge"), max_digits=10, decimal_places=2)
    latitude = models.DecimalField(verbose_name=_("Latitude"), max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(verbose_name=_("Longitude"), max_digits=11, decimal_places=8, null=True, blank=True)

    @property
    def full_address(self):
        """
        Full Address = unit no. + address line 2 + location
        @return: string
        """
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


class OrderFeedback(models.Model):
    """
    Order Feedback model to save feedback's from user in the system

    @requires order_id
    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    order_id = models.ForeignKey(verbose_name=_("Order Id"), to=Order, on_delete=models.PROTECT)
    type = models.CharField(verbose_name=_("Type"), choices=ORDER_FEEDBACK, max_length=100, default=COMPLAINT)
    description = models.TextField(verbose_name=_("Description"))
    mobile = models.CharField(verbose_name=_("User mobile"), max_length=255)

    class Meta:
        verbose_name = _("Order Feedback")
        verbose_name_plural = _("Order Feedback's")

    def __str__(self):
        return self.order_id
