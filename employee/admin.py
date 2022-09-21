from django.contrib import admin

# Register your models here.
from .models import Employee,Bank
admin.site.register([Employee,Bank])