# Generated by Django 4.1.1 on 2022-09-23 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_store_custo_first_n_a7e990_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.collection'),
        ),
    ]
