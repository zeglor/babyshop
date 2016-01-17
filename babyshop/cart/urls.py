from django.conf.urls import url


from .views import view_cart, add_to_cart_async

urlpatterns = [
	# ex: /cart/add_async/
	url(r'^add_async/$', add_to_cart_async, name='add_to_cart_async'),
	url(r'^view/$', view_cart, name='view_cart'),
]
