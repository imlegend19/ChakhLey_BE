from django.db import models
from drfaddons.models import CreateUpdateModel
from django.utils.text import gettext_lazy as _


class PromoCode(CreateUpdateModel):
    from .utils import PromoCodeField
    name = PromoCodeField(verbose_name=_('PromoCode Name'), max_length=10)


class UserPromoCode(CreateUpdateModel):
    """
    Represents promo codes for a specific user

    @author: Yugandhar Desai ("http://github.com/yugi1729")
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
