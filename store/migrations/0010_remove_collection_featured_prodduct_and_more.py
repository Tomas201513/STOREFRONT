# Generated by Django 4.1.1 on 2022-09-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='featured_prodduct',
        ),
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='Products',
            field=models.ManyToManyField(to='store.product'),
        ),
    ]