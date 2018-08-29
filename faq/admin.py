# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


# Register your models here.
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_filter  = ['title']
    search_fields = ["title", "content"]
