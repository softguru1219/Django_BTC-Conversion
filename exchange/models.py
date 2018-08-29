# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid


class CryptoCurrency(models.Model):

    class Meta:
        verbose_name = 'Crypto Currency'
        verbose_name_plural = 'Crypto Currencies'

    code = models.CharField(
        max_length=4,
        unique=True,
        blank=False, help_text=' code of crypto currency')

    name = models.CharField(
        max_length=200,
        blank=False, help_text='name')

    exchange_fee = models.FloatField(default=0.05, blank=False)

    # wallet = models.CharField(
    #     max_length=200,
    #     blank=False, help_text='name')

    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Payment(models.Model):

    order = models.UUIDField(default=uuid.uuid4, editable=False)

    crypto_currency = models.ForeignKey(
        'exchange.CryptoCurrency',
        on_delete=models.CASCADE,
        default=None,
        related_name="crypto_currency")

    payed_amount = models.FloatField(default=1, blank=False)
    received_amount = models.FloatField(default=1, blank=False)

    address = models.CharField(
        max_length=200, help_text='address')

    address_id = models.CharField(
        max_length=36, help_text='address id')

    batch = models.CharField(
        blank=True,
        max_length=200, help_text='BATCH ')

    beneficiary_firstname = models.CharField(
        max_length=200,
        blank=False, help_text='beneficiary first name ')

    beneficiary_lastname = models.CharField(
        max_length=200,
        blank=False, help_text='beneficiary last name ')

    iban = models.CharField(
        max_length=200,
        blank=False, help_text='iban ')

    bic = models.CharField(
        max_length=200,
        blank=False, help_text='bic ')

    payment_purpose = models.CharField(
        max_length=200,
        blank=False, help_text='payment purpose ')

    country = models.CharField(
        max_length=200, default="",
        blank=False, help_text='country')

    email = models.CharField(
        max_length=200, default="",
        blank=False, help_text='country')

    received = models.BooleanField(
        default=False, blank=False)

    verified = models.BooleanField(
        default=False, blank=False)
    sepa_executed = models.BooleanField(
        default=False, blank=False)



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class IpTable(models.Model):

    ip = models.CharField(max_length=20)

    counter = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class SepaCountry(models.Model):
    class Meta:
        verbose_name = 'SEPA Country'
        verbose_name_plural = 'SEPA Countrys'

    country = models.CharField(
        max_length=200,
        blank=False, help_text='country')

    sepa_enable = models.BooleanField(
        default=True, blank=False)

    def __str__(self):
        return self.country



