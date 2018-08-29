# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from news.models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'data']
    list_filter  = ['data']
    search_fields = ["titolo", "contenuto"]

    prepopulated_fields = {"slug": ("titolo",)}
