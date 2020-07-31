# Generated by Django 3.0.8 on 2020-07-29 09:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0037_auto_20200725_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, on_delete=models.SET('deleted_user'), to=settings.AUTH_USER_MODEL),
        ),
    ]