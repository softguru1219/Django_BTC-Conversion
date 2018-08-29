# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from reviews.models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'date', 'stars_support')
    #list_filter = ('nickname', 'review_row')
    search_fields = ["nickname", "review_row"]
