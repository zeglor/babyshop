from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from cart import Cart
from detail.models import Goodie

def add_to_cart_async(request):
	# Get cart object
	cart = Cart(request)
	
	# Decode json request parameters
	data = json.loads(request.body)
	
	product = Goodie.objects.get(pk=data['id'])
	price = product.price
	quantity = data['quantity']
	cart.add(product, price, quantity)
	return JsonResponse({"status": "added"})

def view_cart(request):
	return render(request, 'cart/items.html', {'cart': Cart(request)})
