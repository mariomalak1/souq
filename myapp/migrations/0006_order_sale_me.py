# Generated by Django 3.1 on 2020-10-23 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_product_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sale_me',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mysale', to='myapp.product'),
        ),
    ]
