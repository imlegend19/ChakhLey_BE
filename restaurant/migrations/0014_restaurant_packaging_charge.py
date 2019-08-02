# Generated by Django 2.2 on 2019-08-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_auto_20190724_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='packaging_charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Packaging Charge'),
        ),
    ]
