from django.contrib import admin
from livestock.models import order 

class OrderRep(admin.ModelAdmin):
    list_display = ('Name','Date','Expected_order_recieve_date','Order_Type')

admin.site.register(order, OrderRep)
