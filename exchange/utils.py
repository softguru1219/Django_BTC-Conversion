from coinbase.wallet.client import Client
from django.core.mail import send_mail
import datetime
from django.utils import timezone
from exchange.models import CryptoCurrency

from exchange.models import IpTable

def get_coinbase_client():
    return Client("hzGjPeecxXbxHeve",
                  "ef8UCKF7Trbj9EW2IqDl6k4BJAWlfMaw")


#Chiave API: G8277Re02orcnCka


def get_exchange_rate(crypto_currency):

    client = get_coinbase_client()
    rate = 0;

    if crypto_currency == "BTC":
        rate = client.get_buy_price(currency_pair='BTC-USD')["amount"]
    elif crypto_currency == "LTC":
        rate = client.get_buy_price(currency_pair='LTC-USD')["amount"]
    elif crypto_currency == "ETH":
        rate = client.get_buy_price(currency_pair='ETH-USD')["amount"]
        
    try:
        return str(rate).replace(',','.')
    except Exception as error:
        print error
        return 0



def get_exchange_fee(crypto_currency):

    one_entry = CryptoCurrency.objects.get(code=crypto_currency)

    try:
        return str(one_entry.exchange_fee).replace(',','.')
    except Exception as error:
        print error
        return 0.01


def generate_address():

    client = get_coinbase_client()

    return client.create_address("475201c6-87ea-5635-8ee1-c0100dcff166")


def verify_callback(body, meta):

    client = get_coinbase_client()
    return client.verify_callback(body, meta)


def send_email_payment_notification(payment, url):

    url = url + '/admin/exchange/payment/' + str(payment.id) + '/change/'

    send_mail(
        'New Payment Received on btc2sepa',
        'A new Payment was received: \n\
         Crypto Currency :' + payment.crypto_currency.name + ' \n\
         Payed Amount :' + "{:.9f}".format(payment.payed_amount) + ' ' + payment.crypto_currency.code + ' \n\
         Received Amount ' + "{:.2f}".format(payment.received_amount) + '  USD \n\
         Address ' + payment.address + ' \n\
         User : ' + payment.beneficiary_firstname + ' ' + payment.beneficiary_lastname + ' \n\
         Date : ' + payment.created_at.strftime("%B %d, %Y - %H%m") + ' \n\
         Reason : ' + payment.payment_purpose + ' \n\
         Received: ' + str(payment.received) + ' \n\
         Verified: ' + str(payment.verified) + ' \n\
         Admin URL: ' + url + ' \n\
         ',
        'no-response@btc2sepa.com',
        ['krakiun@gmail.com'],
        fail_silently=False
    )


def get_address_transactions(address_id):
    client = get_coinbase_client()
    return client.get_address_transactions("475201c6-87ea-5635-8ee1-c0100dcff166", address_id)


def check_client_ip(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    iptable,created = IpTable.objects.get_or_create(ip=ip)

    if iptable.counter > 25:
        if iptable.updated_at > timezone.now() - datetime.timedelta(hours=1):
            return False
        else:
            iptable.counter = 0

    else:
        iptable.counter = iptable.counter + 1

    iptable.save()
    return True


