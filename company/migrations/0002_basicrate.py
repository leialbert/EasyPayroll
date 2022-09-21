# Generated by Django 4.1.1 on 2022-09-21 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qhsf_rate', models.FloatField(verbose_name='QHSF Rate')),
                ('cnesst_rate', models.FloatField(verbose_name='CNESST Rate: W')),
                ('wcb_rate', models.FloatField(verbose_name='WCB/WSIB Rate')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
