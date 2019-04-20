from django.db import models
from django.utils.text import gettext_lazy as _


class Category(models.Model):
    from restaurant.models import Restaurant

    name = models.CharField(verbose_name=_('Category'), max_length=200)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant, on_delete=models.PROTECT, unique=False)

    @property
    def product_count(self):
        return Product.objects.all().filter(category_id=self.id).count()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'restaurant')
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(verbose_name=_('Product Name'), max_length=200)
    category = models.ForeignKey(verbose_name=_('Category'), to=Category, on_delete=models.PROTECT)
    is_veg = models.BooleanField(verbose_name=_('Is Veg ?'), default=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)

    @property
    def restaurant(self):
        return self.category.restaurant.id

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'category')
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['id']


class ProductImage(models.Model):

    from .utils import product_image_upload

    name = models.CharField(verbose_name=_('Image Name'), max_length=255)
    product = models.ForeignKey(verbose_name=_('Product'), to=Product, on_delete=models.PROTECT)
    image = models.ImageField(verbose_name=_('Select Image'), upload_to=product_image_upload)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
        ordering = ['id']
