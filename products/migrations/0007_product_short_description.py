# Generated by Django 4.2.6 on 2023-11-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_datetime_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True),
        ),
    ]
