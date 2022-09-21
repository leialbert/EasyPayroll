from django.db import models
from company import models as company_models

# Create your models here.
class PayComponent(models.Model):
    company_id = models.ForeignKey(company_models.Company,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField('Pay Component Name',max_length=120)
    alias_name = models.CharField('Pay Statement Description', max_length=120)
    input_type = models.CharField('Input Type', max_length=20)
    status = models.BooleanField('Enabled?')

    def __str__(self) -> str:
        return super().__str__()
class PayrollSchedule(models.Model):
    company_id = models.ForeignKey(company_models.Company,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField('Name of Pay Cycle', max_length=120)
    frequency = models.CharField('Frequency', max_length=20)
    start_date = models.DateTimeField('First Pay Run Start Date')
    end_date = models.DateTimeField('First Pay Run End Date')
    pay_date = models.DateTimeField('Pay Day')
    status = models.BooleanField('Enabled?')

    def __str__(self) -> str:
        return super().__str__()
