from django.db import models
from drfaddons.models import CreateUpdateModel
from django.utils.text import gettext_lazy as _
from .utils import PromoCodeField


class PromoCode(CreateUpdateModel):
    name = PromoCodeField(verbose_name=_('PromoCode Name'), max_length=10)


