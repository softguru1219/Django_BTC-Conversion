"""btc2sepa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from exchange import views as e_views
from django.conf.urls import ( handler400, handler403, handler404, handler500 )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', e_views.home, name="home"),
    url(r'^exchange/$', e_views.home, name="home"),
    url(r'^exchange/payment', e_views.payment, name="payment"),
    url(r'^exchange/success/(?P<order_id>[0-9a-f-]{36})/$', e_views.success, name="success"),
    url(r'^exchange/limit_exceded', e_views.limit_exceded, name="limit_exceded"),
    url(r'^exchange/callback/$', e_views.callback, name="callback"),
    url(r'^news/', include('news.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^contacts/', e_views.contacts, name='contacts'),
    url(r'^reviews/', include('reviews.urls'), name='reviews'),
    url(r'^send_message/', e_views.send_message, name='send_message'),
    url(r'^get_cryto_curreny_rate_ajax/', e_views.get_cryto_curreny_rate_ajax, name='get_cryto_curreny_rate_ajax'),
]


handler400 = 'exchange.views.page_not_found'
handler403 = 'exchange.views.page_not_found'
handler404 = 'exchange.views.page_not_found'
handler500 = 'exchange.views.bad_request'