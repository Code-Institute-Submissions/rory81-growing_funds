# Generated by Django 3.0.7 on 2020-06-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20200626_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Arts', 'Arts'), ('Charity', 'Charity'), ('Film', 'Film'), ('Food', 'Food'), ('Games', 'Games'), ('Music', 'Music'), ('Publishing', 'Publishing'), ('Technology', 'Technology')], default='No Category Selected', max_length=10),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]