from django.shortcuts import render, get_object_or_404
from .models import Goodie

# Create your views here.

# !! stub
def details(request, goodie_id):
	goodie = get_object_or_404(Goodie, pk=goodie_id)
	context = {'goodie': goodie}
	return render(request, 'detail/details.html', context)
