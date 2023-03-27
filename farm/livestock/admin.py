from django.contrib import admin
from livestock.models import order , stock

class OrderRep(admin.ModelAdmin):
    list_display = ('Name','Date','Expected_order_recieve_date','Order_Type')
    
class stockRep(admin.ModelAdmin):
    list_display = ('label','quantity','unit_price','sold_out')

admin.site.register(order, OrderRep)
admin.site.register(stock, stockRep)
