# Generated by Django 4.1.1 on 2022-09-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
    ]