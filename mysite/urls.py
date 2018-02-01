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

	# /collection/<collection_type>
	url(r'^collection/(?P<collection_type>[a-zA_Z]+)/$', views.collection, name='collection'),

]