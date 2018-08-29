#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.http.request import HttpRequest
from exchange.models import CryptoCurrency
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


class Command(BaseCommand):

	help = 'Add all sepa countrys in db'

	def handle(self, *args, **options):

		cryptocurrency_list = []
		cryptocurrency_list.append({"code": "BTC", "name": "Bitcoin", "exchange_fee": 0.05, "enabled": True })
		cryptocurrency_list.append({"code": "LTC", "name": "Litecoin", "exchange_fee": 0.05, "enabled": True })
		cryptocurrency_list.append({"code": "ETH", "name": "Etherium", "exchange_fee": 0.05, "enabled": True })

		for line in cryptocurrency_list:
			data = CryptoCurrency.objects.create(code=line['code'], name=line['name'], exchange_fee=line['exchange_fee'])

		print "Add successull all default crypto currency"