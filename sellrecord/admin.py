from django.contrib import admin
from .models import Sellrecord

admin.site.site_header = 'Waaneiza Sellrecord Management System'

# Register your models here.
#admin.site.register(Sellrecord)

class SellrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'purchased_items', 'showroom', 'paid', 'date']
    list_filter = ['customer_name', 'customer_phone', 'purchased_items', 'showroom', 'paid', 'date']
    search_fields = ['customer_name', 'customer_phone', 'purchased_items', 'showroom', 'paid', 'date']
admin.site.register(Sellrecord, SellrecordAdmin)
