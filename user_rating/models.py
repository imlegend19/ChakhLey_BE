from django.db import models
from django.utils.text import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from product.models import Product


class UserProductRating(models.Model):
    rating = models.IntegerField(verbose_name=_('Rating'),
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(1),
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

    rating = models.IntegerField(verbose_name=_('Rating'),
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(1),
                                 ])
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant,
                                   on_delete=models.PROTECT)

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = _('Restaurant Rating')
        verbose_name_plural = _('Restaurant Ratings')
        ordering = ['id']
