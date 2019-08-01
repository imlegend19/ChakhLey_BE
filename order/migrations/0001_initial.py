# Generated by Django 2.2 on 2019-04-24 17:04

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        ('product', '0001_initial'),
        ('business', '0002_auto_20190424_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Buyer Name')),
                ('mobile', models.CharField(max_length=15, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('preparation_time',
                 models.DurationField(default=datetime.timedelta(0, 2400), verbose_name='Preparation Time')),
                ('status', models.CharField(
                    choices=[('Pe', 'Pending'), ('Ac', 'Accepted'), ('Pr', 'Preparing'), ('R', 'Ready'),
                             ('Di', 'Dispatched'), ('D', 'Delivered'), ('R', 'Rejected'), ('C', 'Cancelled')],
                    default='Pe', max_length=5, verbose_name='Order Status')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Order Create Date')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='business.Business',
                                               verbose_name='Business')),
                ('restaurant',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.Restaurant',
                                   verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='SubOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product',
                                           verbose_name='Product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.Order',
                                            verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Sub Order',
                'verbose_name_plural': 'Sub Orders',
            },
        ),
        migrations.CreateModel(
            name='DeliveryBoysOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver_boy',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='business.DeliveryBoys',
                                   verbose_name='Delivery Boy')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.Order',
                                            verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Delivery Boys Order Data',
                'verbose_name_plural': 'Delivery Boys Order Data',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='NIIT University', max_length=255, verbose_name='Location')),
                ('unit_no', models.CharField(max_length=100, verbose_name='Unit Number / Floor')),
                ('address_line_2',
                 models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='order.Order',
                                               verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
            },
        ),
    ]
