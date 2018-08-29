from django.conf.urls import url
from . import views as news_views
from django.views.generic import ListView, DetailView
from .models import News




urlpatterns = [
	url(r'^$', ListView.as_view(queryset=News.objects.all().order_by("-data"), 
		template_name = "index.html",
		paginate_by = 6
		), name="ListNews"),

	url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
		model = News,
		template_name="view_news.html"),
		name="singolo"),
]