# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from exchange.models import Payment, CryptoCurrency, IpTable, SepaCountry
# Register your models here.


admin.site.site_header = 'BTC2SEPA ADMIN'

@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'exchange_fee', 'enabled')
    list_filter = ('exchange_fee', 'enabled')
    readonly_fields = ('id',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = ('crypto_currency', 'beneficiary_firstname',
              'beneficiary_lastname','email', 'payed_amount','received_amount', 
              'address','address_id','iban', 'bic', 'payment_purpose', 'country',
              'received', 'verified', 'sepa_executed')

    list_display = ('id', 'crypto_currency', 'beneficiary_firstname',
                    'beneficiary_lastname', 'payed_amount',
                    'received_amount', 'received', 'verified', 'sepa_executed')

    list_filter = ('crypto_currency', 'received', 'verified', 'sepa_executed', 'country')
    readonly_fields = ('order', 'crypto_currency', 'payed_amount', 'received_amount', 
                       'address', 'address_id')

    search_fields = ["beneficiary_lastname", "beneficiary_firstname", "email", "iban"]
    
    # disable add manual payment
    def has_add_permission(self, request):
        return False

    # disable remove permission
    def has_delete_permission(self, request, obj=None):
        return False




@admin.register(IpTable)
class IpTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'counter', 'created_at', 'updated_at')
    readonly_fields = ('id',)
    search_fields = ["ip"]


@admin.register(SepaCountry)
class SepaCountrysAdmin(admin.ModelAdmin):
    list_display = ("country","sepa_enable")
    search_fields = ["country"]
