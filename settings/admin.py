from django.contrib import admin

# Register your models here.
from .models import PayComponent,PayrollSchedule
admin.site.register([PayComponent,PayrollSchedule])