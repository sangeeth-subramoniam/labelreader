# Generated by Django 4.0.2 on 2022-02-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
