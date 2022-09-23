from django.contrib import admin

from .models import Company,Account,PayComponent,Area,Frequency

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name','city','province','country')
    list_display_links = ('name',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','company','username','email','password',)
    list_display_links = ('company','username',)
    list_filter = ('company','username','email',)
    search_fields = ['email','username','company__name']

@admin.register(PayComponent)
class PayComponentAdmin(admin.ModelAdmin):
    list_display = ('category','code','name',)
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('country','country_code','province','province_code',)

@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('country','frequency','periods',)



