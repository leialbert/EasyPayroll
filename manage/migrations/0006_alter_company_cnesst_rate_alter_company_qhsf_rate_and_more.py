# Generated by Django 4.1.1 on 2022-09-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0005_alter_company_account_alter_company_bank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cnesst_rate',
            field=models.FloatField(blank=True, default=0, verbose_name='CNESST Rate: W'),
        ),
        migrations.AlterField(
            model_name='company',
            name='qhsf_rate',
            field=models.FloatField(blank=True, default=0, verbose_name='QHSF Rate'),
        ),
        migrations.AlterField(
            model_name='company',
            name='wcb_rate',
            field=models.FloatField(blank=True, default=0, verbose_name='WCB/WSIB Rate'),
        ),
    ]
