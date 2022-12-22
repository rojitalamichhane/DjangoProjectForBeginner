from django.contrib import admin
from .models import IndustryType, Company

# Register your models here.
admin.site.register(IndustryType)
admin.site.register(Company)