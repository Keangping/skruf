# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'mysite'

urlpatterns = [
	# /
	url(r'^$', views.index, name='index'),

	# /omoss
	url(r'^omoss/$', views.contact, name='contact'),

	# /10-tips-til-bryllupet
	url(r'^10-tips-til-bryllupet/$', views.tips, name='tips'),

	# /slik-skal-dressen-sitte
	url(r'^slik-skal-dressen-sitte/$', views.dressen_sitte, name='dressen_sitte'),

	# /dress-guide-for-menn
	url(r'^dress-guide-for-menn/$', views.dress_guide, name='dress_guide'),

	# /<collection_type>, /dress /skjorte
	# /skreddersydd is here
	url(r'^(?P<collection_type>[a-zA-ZæÆøØåÅ]+)/$', views.collection, name='collection'),

	# /<product_type>/<product_name>, /dress/briz-2-navy **^(?P<cproduct_type_type>[a-zA_Z]+)/(?P<product_name>[a-zA_Z]+)/$
	url(r'^(?P<product_type>[a-zA-ZæÆøØåÅ]+)/(?P<product_name>[\wæÆøØåÅ-]+)/$', views.detail, name='detail'),

]