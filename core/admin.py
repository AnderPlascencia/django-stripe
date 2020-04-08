from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, BillingAddress, Coupon


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'ordered', 
        'being_delivered', 
        'received', 
        'request_refund', 
        'granted_refund',
        'billing_address',
        'payment',
        'coupon'
    ]

    list_display_links = [
        'user',
        'billing_address',
        'payment',
        'coupon'
    ]

    list_filter = [
        'ordered', 
        'being_delivered', 
        'received', 
        'request_refund', 
        'granted_refund'
    ]

    search_fields = [
        'user__username',
        'ref_code'
    ]


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount', 'active']


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(BillingAddress)
admin.site.register(Coupon, CouponAdmin)
