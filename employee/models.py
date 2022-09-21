from django.db import models
from company import models as company_models

# Create your models here.
class Employee(models.Model):
    company_id = models.ForeignKey(company_models.Company,blank=True, null=True,on_delete=models.CASCADE)
    first_name = models.CharField('First Name',max_length=20)
    last_name = models.CharField('Last Name',max_length=20)
    email = models.EmailField('Email')
    employee_type = models.CharField('Employee Type', max_length=10)
    payroll_start_date = models.DateField('Payroll Start Date')
    addr1 = models.CharField('Address Line 1',max_length=120)
    addr2 = models.CharField('Address Line 2',max_length=120)
    zip_code = models.CharField('Zip/Post Code', max_length=20)
    city = models.CharField('City',max_length=20)
    province = models.CharField('Province',max_length=20)
    country = models.CharField('Country',max_length=20)

    def __str__(self) -> str:
        return super().__str__()

class Bank(models.Model):
    employee_id = models.ForeignKey(Employee,blank=True,null=True,on_delete=models.CASCADE)
    bank = models.CharField('Bank Name',max_length=120)
    bk_currency = models.CharField('Currency', max_length=3)
    account = models.CharField('Bank Account', max_length=20)

    def __str__(self) -> str:
        return super().__str__()