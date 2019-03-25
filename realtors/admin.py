from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display= ('id','name','hire_date',)
    list_display_links=('id','name',)
    search_fields=('id','name',)

admin.site.register(Realtor,RealtorAdmin)

