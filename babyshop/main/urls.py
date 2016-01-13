from django.conf.urls import url


from .views import index

urlpatterns = [
	# ex: /
	url(r'^$', index, name='index'),
]
