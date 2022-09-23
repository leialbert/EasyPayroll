# Generated by Django 4.1.1 on 2022-09-23 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='User Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=32, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20, verbose_name='Country Name')),
                ('country_code', models.CharField(max_length=5, unique=True, verbose_name='Country Code')),
                ('province', models.CharField(max_length=20, verbose_name='Province')),
                ('province_code', models.CharField(max_length=5, verbose_name='Province Code')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Company Name')),
            ],
        ),
        migrations.CreateModel(
            name='PayComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, verbose_name='Component Code')),
                ('name', models.CharField(max_length=20, verbose_name='Pay Component')),
                ('category', models.CharField(choices=[('E', 'Earnings'), ('D', 'Deductions')], default='', max_length=10, verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(max_length=20, verbose_name='Frequency')),
                ('periods', models.IntegerField(verbose_name='Period Numbers')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frequency', to='manage.area')),
            ],
        ),
    ]