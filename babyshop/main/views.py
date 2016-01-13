from django.shortcuts import render
from detail.models import Goodie

def index(request):
	goodies = Goodie.objects.all()
	context = {'goodies': goodies}
	return render(request, 'main/index.html', context)
