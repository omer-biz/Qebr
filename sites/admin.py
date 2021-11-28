from django.contrib import admin

from .models import Deceased, Afocha

# Register your models here.

@admin.register(Deceased)
class DeceasedDefinded(admin.ModelAdmin):
    list_display = ('full_name', 'role_num', 'grave_number', 'qebele', 'afocha_name', 'dod')

admin.site.register(Afocha)
