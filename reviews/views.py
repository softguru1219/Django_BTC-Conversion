# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *

# Create your views here.

def reviews(request):

    reviews = Reviews.objects.all()

    review_count = Reviews.objects.count()
    speed_avg = Reviews.objects.all().aggregate(Avg('stars_speed'))['stars_speed__avg']
    support_avg = Reviews.objects.all().aggregate(Avg('stars_support'))['stars_support__avg']
    stars_avg = Reviews.objects.all().aggregate(Avg('stars_experience'))['stars_experience__avg']

    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 10)
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    for review in reviews:
        speed = int(round(float(review.stars_speed)))
        review.speed_rest = range(0, 5-speed)
        review.stars_speed = range(0, speed)

        support = int(round(float(review.stars_support)))
        review.support_rest = range(0, 5-support)
        review.stars_support = range(0, support)

        experience = int(round(float(review.stars_experience)))
        review.experience_rest = range(0, 5-experience)
        review.stars_experience = range(0, experience)

    return render(
        request, 'reviews.html',
        {
            'reviews': reviews,
            'review_count': review_count,
            'speed_avg': round(float(speed_avg), 2),
            'support_avg': round(float(support_avg), 2),
            'stars_avg': round(float(stars_avg), 2),
        }
    )
