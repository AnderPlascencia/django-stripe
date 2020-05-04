from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Address, Coupon, Refund


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(request_refund=False, granted_refund=True)


make_refund_accepted.short_description = "Grant refund"


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'request_refund',
        'granted_refund',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]

    list_display_links = [
        'user',
        'shipping_address',
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
    actions = [make_refund_accepted]


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount', 'active']


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip_code',
        'address_type',
        'default',
    ]
    list_filter = ['country', 'default', 'address_type']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip_code']

    class Meta:
        verbose_name_plural = 'addresses'


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Address, AddressAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Refund)
