#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.http.request import HttpRequest
from exchange.utils import get_coinbase_client, get_address_transactions
from exchange.utils import send_email_payment_notification
from exchange.models import Payment
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


class Command(BaseCommand):

    help = ''

    def handle(self, *args, **options):

        payments = Payment.objects.all()
        client = get_coinbase_client()

        for payment in payments:
            tx = get_address_transactions(payment.address_id)

            try:
                if tx["data"]["status"] == "completed" and not payment.received:
                    payment.received = True
                    payment.save()
                    send_email_payment_notification(payment, "")

            except TypeError:
                pass
            except Exception as error:
                print error
                # TODO: Track this too?
        else:
              print "Not present new payments"


