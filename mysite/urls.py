from django.conf.urls import url
from . import views

app_name = 'mysite'

urlpatterns = [
	# /
	url(r'^$', views.index, name='index'),

	# /omoss
	url(r'^omoss/$', views.contact, name='contact'),

	

]