from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, BillingAddress, Coupon


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount', 'active']


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(BillingAddress)
admin.site.register(Coupon, CouponAdmin)
