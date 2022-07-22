from django.contrib import admin
from .models import Employees, Companies
# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model= Employees
    extra= 3 
    
class CompaniesAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields': ['companies_num']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display= ('companies_num', 'pub_date', 'was_published_recently')
    list_filter= ['pub_date']
    search_fields = ['companies_id']
    
    
    inlines= [ChoiceInLine]
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Employees)