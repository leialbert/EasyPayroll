# Generated by Django 4.1.1 on 2022-09-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name of Pay Cycle')),
                ('frequency', models.CharField(max_length=20, verbose_name='Frequency')),
                ('start_date', models.DateTimeField(verbose_name='First Pay Run Start Date')),
                ('end_date', models.DateTimeField(verbose_name='First Pay Run End Date')),
                ('pay_date', models.DateTimeField(verbose_name='Pay Day')),
                ('status', models.BooleanField(verbose_name='Enabled?')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
