from django.db import models
from django.contrib.auth.admin import UserAdmin

# Create your models here.
class Company(models.Model):
    currency_choice = [('CAD','CAD'),('USD','USD'),('CNY','CNY')]
    name = models.CharField('Company Name', max_length=120)
    tel  = models.CharField('Telephone',blank=True, max_length=20)
    email = models.EmailField('Email',blank=True)
    website = models.URLField('Website',blank=True)
    addr1 = models.CharField('Address Line 1',blank=True,max_length=120)
    addr2 = models.CharField('Address Line 2',blank=True,max_length=120)
    zip_code = models.CharField('Zip/Post Code',blank=True, max_length=20)
    city = models.CharField('City',blank=True,max_length=20)
    province = models.CharField('Province',max_length=20)
    country = models.CharField('Country',max_length=20)
    bank = models.CharField('Bank Name',blank=True,max_length=120)
    bk_currency = models.CharField('Currency', blank=True,choices=currency_choice ,max_length=3)
    account = models.CharField('Bank Account', blank=True,max_length=20)
    qhsf_rate = models.FloatField('QHSF Rate',blank=True, default=0)
    cnesst_rate = models.FloatField('CNESST Rate: W',blank=True,default=0)
    wcb_rate = models.FloatField('WCB/WSIB Rate',blank=True,default=0)

    def __str__(self):
        return self.name
class Account(models.Model):
    company = models.ForeignKey(Company,related_name='client_user',null=True,blank=True,on_delete=models.CASCADE)
    username = models.CharField('User Name',max_length=20,null=True,blank=True)
    email = models.EmailField('Email',unique=True,null=True,blank=True)
    password = models.CharField('Password',max_length=32,null=True,blank=True)
    def __str__(self):
        return self.username
class PayComponent(models.Model):
    category_choice = [('E','Earnings'),('D','Deductions')]
    code = models.CharField('Component Code',max_length=5)
    name = models.CharField('Pay Component', max_length=20)
    category = models.CharField('category',choices=category_choice,max_length=10,default='')
    def __str__(self):
        return self.name
class Area(models.Model):
    country = models.CharField('Country Name', max_length=20)
    country_code = models.CharField('Country Code',max_length=5,unique=True)
    province = models.CharField('Province',max_length=20)
    province_code = models.CharField('Province Code', max_length=5)
    def __str__(self):
        return self.country
class Frequency(models.Model):
    country = models.ForeignKey(Area, related_name='frequency',on_delete=models.CASCADE,null=True,blank=True)
    frequency = models.CharField('Frequency',max_length=20)
    periods = models.IntegerField('Period Numbers')
    def __str__(self):
        return self.frequency

