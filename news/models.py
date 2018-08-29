# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.


class News(models.Model):
	titolo = models.CharField(max_length=120)
	contenuto = models.TextField()
	data = models.DateTimeField(auto_now=False, auto_now_add=True)
	slug = models.SlugField()

	def __str__(self):
		return self.titolo


	def get_absolute_url(self):
		return reverse("singolo", kwargs={"id": self.id, "slug" : self.slug})
