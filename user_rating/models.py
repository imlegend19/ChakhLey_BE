from django.db import models
from django.utils.text import gettext_lazy as _
from rest_framework.compat import MaxValueValidator, MinValueValidator

from product.models import Product


class UserProductRating(models.Model):
    rating = models.DecimalField(verbose_name=_('Rating'), max_digits=1, decimal_places=1,
                                 validators=[
                                     MaxValueValidator(5.0),
                                     MinValueValidator(0.0)
                                 ])
    product = models.ForeignKey(verbose_name=_('Product'), to=Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = _('Product Rating')
        verbose_name_plural = _('Product Ratings')
        ordering = ['id']


class UserRestaurantRating(models.Model):
    from restaurant.models import Restaurant

    rating = models.DecimalField(verbose_name=_('Rating'), max_digits=1, decimal_places=1,
                                 validators=[
                                     MaxValueValidator(5.0),
                                     MinValueValidator(0.0)
                                 ])
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant,
                                   on_delete=models.PROTECT)

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = _('Restaurant Rating')
        verbose_name_plural = _('Restaurant Ratings')
        ordering = ['id']


