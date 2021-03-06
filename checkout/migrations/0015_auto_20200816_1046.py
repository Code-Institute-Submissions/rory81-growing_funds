# Generated by Django 3.0.8 on 2020-08-16 10:46

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20200816_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_pledged',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('1.00'))], verbose_name='Amount'),
        ),
    ]
