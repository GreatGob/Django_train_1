from django.contrib import admin

from list.models import Companies, Employees, Details

# Register your models here.
admin.site.register(Companies)
admin.site.register(Employees)
admin.site.register(Details)