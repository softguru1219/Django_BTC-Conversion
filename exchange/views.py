from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage


from exchange.models import Payment, CryptoCurrency, SepaCountry
from exchange.utils import get_exchange_rate, generate_address, get_exchange_fee
from exchange.utils import send_email_payment_notification, verify_callback
from exchange.utils import check_client_ip
import uuid
import json
import requests
import smtplib

from django.shortcuts import ( render_to_response )
from django.template import RequestContext


@require_http_methods("GET")
def home(request):

    crypto_currency = request.GET.get('crypto_currency', "BTC")

    rate = get_exchange_rate(crypto_currency)
    exchange_fee = get_exchange_fee(crypto_currency)

    return render(request, 'home.html', {
        'rate': rate,
        'exchange_fee' : exchange_fee,
        'crypto_currency': crypto_currency,
        'crypto_currencies': CryptoCurrency.objects.all(),
        'sepa_countrys' : SepaCountry.objects.all(),
    })

def get_cryto_curreny_rate_ajax(request):

    crypto_currency = request.GET['crypto_currency']
    rate = get_exchange_rate(crypto_currency)
    data = {}
    data["rate"] = rate
    return JsonResponse(data)

@require_http_methods(["GET", "POST"])
def payment(request):

    # if check_client_ip(request):

        code = request.POST.get('crypto_currency', "BTC")
        crypto_currency = CryptoCurrency.objects.get(code=code)
        rate = get_exchange_rate(crypto_currency)

        payed_amount = float(request.POST.get('payed_amount', 0))
        temp = payed_amount * float(rate)
        received_amount = temp - (temp * 0.05)

        b_firstname = request.POST.get('b_firstname', "")
        b_lastname = request.POST.get('b_lastname', "")
        iban = request.POST.get('iban', "")
        bic = request.POST.get('bic', "")
        payment_purpose = request.POST.get('payment_purpose', "")
        email = request.POST.get('email', "")
        country = request.POST.get('country', "")

        address_obj = generate_address()
        payment = Payment.objects.create(
            order=uuid.uuid4(),
            crypto_currency=crypto_currency,
            payed_amount=payed_amount,
            received_amount=received_amount,
            address=address_obj["address"],
            address_id=address_obj["id"],
            batch="",
            beneficiary_firstname=b_firstname,
            beneficiary_lastname=b_lastname,
            iban=iban,
            bic=bic,
            payment_purpose=payment_purpose,
            email=email,
            country=country)
        return render(
            request,
            'payment.html',
            {
                'order_id': payment.order,
                'address': payment.address,
                'crypto_currency': payment.crypto_currency,
                'payed_amount': payment.payed_amount,
                'rate': rate,
                'uri_path': request.build_absolute_uri().replace(request.get_full_path(), "")
            })

    # else:
    #     return redirect('limit_exceded')


def limit_exceded(request):
    return render(request, 'limit_exceded.html',{})


@require_http_methods(["GET"])
def success(request, order_id):

    payment = Payment.objects.get(order=order_id)

    return render(
        request,
        'success.html',
        {
            'order_id': payment.order,
            'date': payment.created_at.strftime("%B %d, %Y %H:%m"),
            'payed_amount': payment.payed_amount,
            'received_amount': payment.received_amount,
            'address': payment.address,
            'batch': payment.batch,
            'crypto_currency': payment.crypto_currency,
            'uri_path': request.build_absolute_uri().replace(request.get_full_path(), ""),
            'verified': payment.verified,
        })

def contacts(request):
    return render(request, 'contact.html')

def get_client_ip(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if client_ip:
        ip = client_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_message(request):

    email = request.POST['email']
    content = request.POST['content']
    app_num = request.POST['app_num']

    get_request = request.POST["g-recaptcha-response"]
    url = "https://www.google.com/recaptcha/api/siteverify"
    my_param = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': get_request,
        'remoteip': get_client_ip(request)
    }
    verify = requests.get(url, params=my_param, verify=True).json()
    status = verify.get("success", False)

    if not status:
        message = 'Captcha Validation Failed. Please Try again!'
        return render(request, 'contact.html', {"message": message})
    else:
        subject = "Bitcoin2sepa Support"
        to = ['romeo.bejan1118@gmail.com']
        from_email = email

        message = 'Application Number: {num}</br>Content: {content}'.format(num=app_num, content=content)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()

        # send_mail('caption', 'this is exam content', 'try.best0007@gmail.com', ['romeo.bejan1118@gmail.com'])
        messagea = "Email sent!"
        return render(request, 'contact.html', {"message": messagea})

@require_http_methods(["POST"])
@csrf_exempt
def callback(request):

    try:
        verified = verify_callback(request.body, request.META['CB-SIGNATURE'])
    except:
        verified = False

    if verified or settings.DEBUG:

        try:
            addr = json.loads(request.body)["data"]["address"]
            payment = Payment.objects.get(address=addr)

            if not payment.received:
                payment.received = True
                payment.save()

                url = request.build_absolute_uri().replace(request.get_full_path(), "")
                send_email_payment_notification(payment, url)

        except:
            # TODO: Track this error?
            return HttpResponse(status=400)

        return HttpResponse(addr, status=200)


# HTTP Error 500
def bad_request(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response


# HTTP Error 500
def page_not_found(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response

