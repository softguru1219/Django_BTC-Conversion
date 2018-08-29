# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

# Create your views here.

def faq(request):

    faqs = Faq.objects.all()

    return render(request, 'faq.html', {'faqs': faqs})
