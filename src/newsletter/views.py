from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "base.html", {})

def carousel(request):
	return render(request, "carousel.html", {})


def item(request):
	return render(request, "product_item.html", {})

def index(request):
	return render(request, "index.html", {})

def contact(request):
	return render(request, "contact.html", {})