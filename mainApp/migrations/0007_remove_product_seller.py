# Generated by Django 4.0.1 on 2022-02-09 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_alter_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
    ]
