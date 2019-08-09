# Generated by Django 2.2 on 2019-08-09 08:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('unit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Unit No')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('website', models.URLField(blank=True, max_length=255, null=True, verbose_name='Website / Online Listing Link')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('cost_for_two', models.CharField(choices=[('$', '100'), ('$$', '100 - 400'), ('$$$', '400 - 800'), ('$$$$', '800 - 1500'), ('$$$$$', '1500+')], max_length=255, verbose_name='Cost For Two')),
                ('establishment', models.CharField(choices=[('Ca', 'Casual Dining'), ('Fi', 'Fine Dining'), ('Fo', 'Food Court'), ('Qu', 'Quick Bites'), ('De', 'Dessert Parlor'), ('B', 'Bakery'), ('Sw', 'Sweet Shop'), ('Cf', 'Café'), ('Dh', 'Dhaba'), ('Br', 'Bar'), ('Me', 'Meat Shop'), ('Be', 'Beverage Shop'), ('Pu', 'Pub'), ('Ki', 'Kiosk'), ('Lo', 'Lounge'), ('Mi', 'Microbrewery'), ('Cl', 'Club'), ('Fd', 'Food Truck'), ('Co', 'Confectionery'), ('Cc', 'Cocktail'), ('Ir', 'Irani Café'), ('Ms', 'Mess'), ('Ju', 'Juice'), ('Wi', 'Wine Bar'), ('Po', 'Pop Up')], max_length=255, verbose_name='Establishment')),
                ('delivery_time', models.IntegerField(default=40, verbose_name='Delivery Time')),
                ('is_veg', models.BooleanField(default=True, verbose_name='Is Veg?')),
                ('commission', models.IntegerField(default=10, verbose_name='Commission')),
                ('open_from', models.TimeField(default=datetime.time(11, 30), verbose_name='Open From')),
                ('open_till', models.TimeField(default=datetime.time(23, 0), verbose_name='Open Till')),
                ('latitude', models.DecimalField(decimal_places=8, default=27.978237, max_digits=10, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=8, default=76.4000549, max_digits=11, verbose_name='Longitude')),
                ('discount', models.IntegerField(default=0, verbose_name='Discount')),
                ('packaging_charge', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Packaging Charge')),
                ('gst', models.BooleanField(default=False, verbose_name='GST Charge')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.Area', verbose_name='Area')),
                ('business', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='business.Business', verbose_name='Business')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
                'ordering': ['-commission'],
            },
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('image_type', models.CharField(choices=[('Re', 'Restaurant'), ('Ki', 'Kitchen'), ('La', 'Landmark'), ('Fo', 'Food'), ('L', 'Logo')], default='Re', max_length=255, verbose_name='Image Type')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Select Image')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.Restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Restaurant Image',
                'verbose_name_plural': 'Restaurant Images',
            },
        ),
        migrations.CreateModel(
            name='RestaurantCuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(choices=[('As', 'Asian'), ('C', 'Cafe'), ('Ch', 'Chinese'), ('Co', 'Continental'), ('Ff', 'Fast Food'), ('Fi', 'Finger Food'), ('G', 'Grill'), ('In', 'Indian'), ('It', 'Italian'), ('Ja', 'Japanese'), ('Le', 'Lebanese'), ('Mi', 'Mithai'), ('Mu', 'Mughlai'), ('Ni', 'North Indian'), ('Ra', 'Rajasthani'), ('Si', 'South Indian'), ('Sf', 'Street Food'), ('Su', 'Sushi')], max_length=255, verbose_name='Cuisine')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.Restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Restaurant Cuisine',
                'verbose_name_plural': 'Restaurant Cuisines',
            },
        ),
    ]
