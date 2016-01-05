from django.conf.urls import url

from .views import details

urlpatterns = [
	#url(r'^$', details, name='details'),
	# ex: /detail/1
	url(r'^(?P<goodie_id>[0-9]+)/$', details, name='details'),
]
