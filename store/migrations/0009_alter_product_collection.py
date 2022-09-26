# Generated by Django 4.1.1 on 2022-09-25 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_address_options_alter_cart_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(blank=True, default=models.CharField(max_length=255), null=True, on_delete=django.db.models.deletion.PROTECT, to='store.collection'),
        ),
    ]