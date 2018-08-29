# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Reviews(models.Model):
	class Meta:
	    verbose_name = 'Review'
	    verbose_name_plural = 'Reviews'

	nickname = models.CharField(
	    max_length=200,
	    blank=False, help_text='nickname')

	review_row       = models.TextField()

	stars_support    = models.CharField(max_length=100, default='5')
	stars_speed      = models.CharField(max_length=100, default='5')
	stars_experience = models.CharField(max_length=100, default='5')


	date = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
	    return self.nickname