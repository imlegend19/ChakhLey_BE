# Generated by Django 2.2 on 2019-07-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0006_productcombo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcombo',
            name='image',
            field=models.ImageField(default=None, upload_to='combos/', verbose_name='Select Image'),
        ),
    ]
