# Generated by Django 3.0.7 on 2020-07-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20200704_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='conditions',
            field=models.BooleanField(default=False),
        ),
    ]