from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import gettext_lazy as _

from restaurant.models import Restaurant


class Category(models.Model):
    name = models.CharField(verbose_name=_('Category'), max_length=255)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    name = models.CharField(verbose_name=_('Product Name'), max_length=255)
    category = models.ForeignKey(verbose_name=_('Category'), to=Category, on_delete=models.PROTECT)
    is_veg = models.BooleanField(verbose_name=_('Is Veg ?'), default=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


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


class UserRestaurantRating(models.Model):
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


class ProductImage(models.Model):

    from .utils import product_image_upload

    name = models.CharField(verbose_name=_('Image Name'), max_length=255)
    product = models.ForeignKey(verbose_name=_('Product'), to=Product, on_delete=models.PROTECT)
    image = models.ImageField(product_image_upload)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
