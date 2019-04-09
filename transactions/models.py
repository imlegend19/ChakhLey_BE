from django.db import models
from drfaddons.models import CreateUpdateModel

from django.utils.text import gettext_lazy as _

from ChakhLe_BE.variables import COD, CASH


class OrderPayment(CreateUpdateModel):
    from ChakhLe_BE.variables import PAYMENT_MODE_CHOICES, PAYMENT_TYPE_CHOICES

    from order.models import Order
    from business.models import DeliveryBoys

    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, verbose_name=_('Order'))
    amount = models.DecimalField(verbose_name=_("Amount"), max_digits=10, decimal_places=2)
    is_credit = models.BooleanField(verbose_name=_("Is Credit?"), default=True,
                                    help_text=_("Is payment towards system?"))
    payment_type = models.CharField(verbose_name=_("Payment Type"), choices=PAYMENT_TYPE_CHOICES,
                                    default=COD, max_length=5)
    payment_mode = models.CharField(verbose_name=_("Payment Mode"), choices=PAYMENT_MODE_CHOICES,
                                    default=CASH, max_length=5)
    accepted_by = models.ForeignKey(to=DeliveryBoys, on_delete=models.PROTECT, verbose_name=_("Payment Accepted By"),
                                    null=True, blank=True)

    def __str__(self):
        return str(self.order) + " - " + str(self.amount)

    class Meta:
        verbose_name = _('Order Payment')
        verbose_name_plural = _('Order Payments')
