from django.contrib import admin

# Register your models here.
from .models import Company,Bank,BasicRate
admin.site.register([Company,Bank,BasicRate])