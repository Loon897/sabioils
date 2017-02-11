from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "base2.html", {})

def carousel(request):
	return render(request, "carousel.html", {})


def item(request):
	return render(request, "product_item.html", {})