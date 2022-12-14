# Generated by Django 4.1.1 on 2022-09-25 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_collection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['street']},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ['cart']},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['payment_status']},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['product']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='promotion',
            options={'ordering': ['description']},
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.collection'),
        ),
    ]
