# Generated by Django 4.2.4 on 2023-09-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_vehicles_capacity_remove_vehicles_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
