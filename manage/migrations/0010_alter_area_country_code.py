# Generated by Django 4.1.1 on 2022-09-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0009_alter_area_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='country_code',
            field=models.CharField(choices=[('CAN', 'CAN'), ('USA', 'USA'), ('CHN', 'CHN')], max_length=5, verbose_name='Country Code'),
        ),
    ]
