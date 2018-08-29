#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.http.request import HttpRequest
from exchange.models import SepaCountry
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


class Command(BaseCommand):

    help = 'Add all sepa countrys in db'

    def handle(self, *args, **options):

		countryss = ['Aland Islands','Austria','Azores','Belgium','Bulgaria','Canary Islands','Croatia','Cyprus','Czech Republic','Denmark',
					'Estonia','Finland','France','French Guiana','Germany','Gibraltar','Greece','Guadeloupe','Guernsey','Hungary','Iceland',
					'Ireland','Isle of Man','Italy','Jersey','Latvia','Liechtenstein','Lithuania','Luxembourg','Madeira','Malta','Martinique',
					'Mayotte','Monaco','Netherlands','Norway','Poland','Portugal','Réunion','Romania','Saint Barthélemy','Saint Martin (French part)',
					'Saint Pierre and Miquelon','San Marino','Slovakia','Slovenia','Spain','Sweden','Switzerland','United Kingdom']

		for line in countryss:
			data = SepaCountry.objects.create(country=line, sepa_enable=True)

		print "Add successull all sepa country"
