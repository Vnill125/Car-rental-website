# Generated by Django 4.2.4 on 2023-10-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_order_endrent_alter_order_startrent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='contact_phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]