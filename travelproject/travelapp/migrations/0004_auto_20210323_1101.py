# Generated by Django 3.1.7 on 2021-03-23 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='month',
            field=models.CharField(max_length=100),
        ),
    ]
