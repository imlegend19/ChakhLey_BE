from django.db import models
from django.utils.text import gettext_lazy as _


class Category(models.Model):
    from restaurant.models import Restaurant

    name = models.CharField(verbose_name=_('Category'), max_length=200)
    restaurant = models.ForeignKey(verbose_name=_('Restaurant'), to=Restaurant, on_delete=models.PROTECT, unique=False)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    @property
    def product_count(self):
        return Product.objects.all().filter(category_id=self.id).count()

    @property
    def products(self) -> list:

        products = []
        for i in Product.objects.filter(category=self.id):
            x = {'id': i.id, 'name': i.name, 'category': i.category.id, 'is_veg': i.is_veg, 'price': i.price,
                 'discount': i.discount, 'inflation': i.inflation, 'active': i.active, 'image_url': i.image_url,
                 'description': i.description, 'restaurant': i.restaurant, 'recommended_product': i.recommended_product,
                 'display_price': i.display_price, 'packaging_charge': i.packaging_charge}
            products.append(x)

        return products

    @property
    def combos(self):
        from django.forms.models import model_to_dict

        combos = []
        if self.name == 'Combos':
            for i in ProductCombo.objects.filter(restaurant=self.restaurant.id):
                combos.append(model_to_dict(i))

            return combos

    @property
    def veg_products(self):

        veg_products = []
        for i in Product.objects.filter(category=self.id):
            if i.is_veg:
                x = {'id': i.id, 'name': i.name, 'category': i.category.id, 'is_veg': i.is_veg, 'price': i.price,
                     'discount': i.discount, 'inflation': i.inflation, 'active': i.active, 'image_url': i.image_url,
                     'description': i.description, 'restaurant': i.restaurant,
                     'recommended_product': i.recommended_product, 'packaging_charge': i.packaging_charge,
                     'display_price': i.display_price}
                veg_products.append(x)

        return veg_products

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'restaurant')
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(verbose_name=_('Product Name'), max_length=200)
    category = models.ForeignKey(verbose_name=_('Category'), to=Category, on_delete=models.PROTECT,
                                 related_name='product')
    is_veg = models.BooleanField(verbose_name=_('Is Veg ?'), default=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)
    discount = models.IntegerField(verbose_name=_('Discount'), default=0)
    inflation = models.IntegerField(verbose_name=_('Inflation'), default=0)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    image = models.ImageField(verbose_name=_('Select Image'), upload_to='products/')
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    packaging_charge = models.DecimalField(verbose_name=_("Packaging Charge"), default=0, max_digits=10,
                                           decimal_places=2)

    @property
    def restaurant(self):
        return self.category.restaurant.id

    @property
    def image_url(self):
        from django.contrib.sites.models import Site

        domain = Site.objects.get_current().domain
        url = 'http://{domain}'.format(domain=domain)

        if self.image and hasattr(self.image, 'url'):
            return url + self.image.url

    @property
    def recommended_product(self):
        if self.image:
            return True
        else:
            return False

    @property
    def display_price(self):
        discounted_price = float(self.price) - (float(self.price) * (self.discount / 100))
        inflated_price = discounted_price + (discounted_price * (self.inflation / 100))

        return inflated_price

    def __str__(self):
        return self.name + ' - ' + self.category.restaurant.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductCombo(models.Model):
    from restaurant.models import Restaurant

    name = models.CharField(verbose_name=_("Combo Name"), max_length=255)
    price = models.DecimalField(verbose_name=_('Combo Price'), max_digits=10, decimal_places=2)
    products = models.ManyToManyField(verbose_name=_('Products'), to=Product)
    restaurant = models.ForeignKey(verbose_name=_("Restaurant"), to=Restaurant, on_delete=models.PROTECT)
    discount = models.IntegerField(verbose_name=_('Discount'), default=0)
    inflation = models.IntegerField(verbose_name=_('Inflation'), default=0)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    image = models.ImageField(verbose_name=_('Select Image'), upload_to='combos/', default=None)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)

    @property
    def display_price(self):
        discounted_price = self.price - (self.price * (self.discount / 100))
        inflated_price = discounted_price + (discounted_price * (self.inflation / 100))

        return inflated_price

    @property
    def actual_price(self):
        tot = 0

        for i in self.products.all():
            tot += i.display_price

        return tot

    def save(self, *args, **kwargs):
        is_new = self.id is None
        super(ProductCombo, self).save(force_insert, force_update)
        if is_new:
            if Category.objects.filter(name='Combos').exists():
                print("Already exists!")
            else:
                Category.objects.create(name='Combos', restaurant=self.restaurant)
                print("Category created!")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Combo")
        verbose_name_plural = _("Combos")
