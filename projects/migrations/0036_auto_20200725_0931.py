# Generated by Django 3.0.8 on 2020-07-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_auto_20200717_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='backers_story',
        ),
        migrations.AddField(
            model_name='project',
            name='backers_story_option1',
            field=models.TextField(default='if you back this project you will ', max_length=5000),
        ),
        migrations.AddField(
            model_name='project',
            name='backers_story_option2',
            field=models.TextField(default='if you back this project you will ', max_length=5000),
        ),
        migrations.AddField(
            model_name='project',
            name='backers_story_option3',
            field=models.TextField(default='if you back this project you will ', max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
