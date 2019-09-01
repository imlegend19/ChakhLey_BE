from django.db import models
from drfaddons.models import CreateUpdateModel
from django.utils.text import gettext_lazy as _
from ChakhLey_BE.variables import *


class Offer(CreateUpdateModel):
    """
    Represents general offers in the system.

    @author: Mahen Gandhi (https://github.com/imlegend19)
    """
    from .utils import OfferField

    code = OfferField(verbose_name=_('Offer Code'), max_length=10)
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    type = models.CharField(verbose_name=_('Offer Type'), choices=OFFER_TYPE, max_length=255, default=DISCOUNT)
    description = models.TextField(verbose_name=_('Description'))
    valid_from = models.DateTimeField(verbose_name=_('Valid From'))
    valid_till = models.DateTimeField(verbose_name=_('Valid Till'))
    banner = models.TextField(verbose_name=_('Banner'))
    free_delivery = models.BooleanField(verbose_name=_('Free Delivery'), default=False)
    discount = models.IntegerField(verbose_name=_('Discount'), null=True, blank=True)
    max_user_usage = models.IntegerField(verbose_name=_('Max User Usage'), default=1)
    day = models.CharField(verbose_name=_('Offer Day'), choices=DAYS, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')

    def clean(self, *args, **kwargs):
        from django.core.exceptions import ValidationError

        if self.valid_till <= self.valid_from:
            raise ValidationError('Valid Till should be more than Valid From.')

        if self.type == DISCOUNT and self.discount is None:
            if self.day is not None:
                raise ValidationError("Warning: 'day' field has no effect on this offer.")
            else:
                raise ValidationError("'discount' field cannot be null.")

        if self.type == FREE_DELIVERY and self.free_delivery is False:
            if self.day is not None:
                raise ValidationError("Warning: 'day' field has no effect on this offer.")
            else:
                raise ValidationError("'free_delivery' field should be True for this offer.")

        if self.type == DAY_COUPON and self.day is None:
            if self.discount is not None:
                raise ValidationError("Warning: 'discount' field has no effect on this offer.")
            else:
                raise ValidationError("'day' cannot be null for this offer.")

        super(Offer, self).clean()

    @property
    def expired(self) -> bool:
        import pytz
        import datetime

        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.datetime.now().astimezone(tz)

        if now <= self.valid_from or now >= self.valid_till:
            return False
        else:
            return True


class UserPromoCode(CreateUpdateModel):
    """
    Represents promo codes for a specific user

    @author: Yugandhar Desai ("https://github.com/yugi1729")
    """
    from .utils import PromoCodeField
    from drf_user.models import User

    code = PromoCodeField(verbose_name=_('User Promo code'), max_length=10)
    desc = models.TextField(verbose_name=_('Promo code description'), )
    user = models.ForeignKey(verbose_name=_('User'), to=User, on_delete=models.PROTECT)
    discount = models.IntegerField(verbose_name=_('Discount'), null=True, blank=True)
    minimum_order = models.FloatField(verbose_name=_('Minimum order'), default=200, )
    valid_from = models.DateTimeField(_('Valid from date'))
    valid_till = models.DateTimeField(_('Valid till date'))
    max_uses = models.IntegerField(verbose_name=_('Maximum Uses'), default=1)
    uses = models.IntegerField(verbose_name=_('Number of uses'), default=0)
    free_delivery = models.BooleanField(verbose_name=_('free delivery status'), default=False)
    date_created = models.DateField(verbose_name=_('Date created'))
    asset = models.ImageField(verbose_name=_('Promo Code Image'), upload_to='promo/')

    class Meta:
        ordering = ['-id']
        verbose_name = _("User Promo Code")
        verbose_name_plural = _("User Promo Codes")

    @property
    def banner(self):
        msg = "Congratulations You have received a special offer! Use {0} to get ".format(self.code)
        if self.discount is not None and self.free_delivery is False:
            msg += "{0}% discount on your next ".format(self.discount)
            if self.max_uses == 1:
                msg += "order."
            else:
                msg += "{0} orders.".format(self.max_uses)

            return msg
        elif self.discount is None and self.free_delivery is True:
            msg += "free delivery on your next"
            if self.max_uses == 1:
                msg += "order."
            else:
                msg += "{0} orders.".format(self.max_uses)
            return msg
        elif self.free_delivery is True and self.discount is not None:
            msg += "special offer and free delivery  on your next"
            if self.max_uses == 1:
                msg += "order."
            else:
                msg += "orders."

        else:
            return None

    @property
    def is_valid(self) -> bool:
        import pytz
        import datetime

        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.datetime.now().astimezone(tz)

        if now <= self.valid_from or now >= self.valid_till:
            return False
        else:
            return True
