# Generated by Django 4.0.2 on 2022-02-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_barcode_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_similarity_checked',
            field=models.IntegerField(default=0),
        ),
    ]
