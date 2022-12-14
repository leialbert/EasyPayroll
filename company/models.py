from django.db import models

# Create your models here.
class Company(models.Model):
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

    def __str__(self) -> str:
        return super().__str__()
class Bank(models.Model):
    company_id = models.ForeignKey(Company,blank=True,null=True,on_delete=models.CASCADE)
    bank = models.CharField('Bank Name',max_length=120)
    bk_currency = models.CharField('Currency', max_length=3)
    account = models.CharField('Bank Account', max_length=20)

    def __str__(self) -> str:
        return super().__str__()

class BasicRate(models.Model):
    company_id = models.ForeignKey(Company,blank=True,null=True,on_delete=models.CASCADE)
    qhsf_rate = models.FloatField('QHSF Rate')
    cnesst_rate = models.FloatField('CNESST Rate: W')
    wcb_rate = models.FloatField('WCB/WSIB Rate')

    def __str__(self) -> str:
        return super().__str__()