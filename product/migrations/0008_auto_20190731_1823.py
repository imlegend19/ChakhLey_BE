# Generated by Django 2.2 on 2019-07-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0007_auto_20190731_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/', verbose_name='Select Image'),
        ),
    ]
