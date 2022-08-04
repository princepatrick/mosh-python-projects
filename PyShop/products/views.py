from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


# Create your views here.
def index(request):
    prs = Products.objects.all()
    return render(request, 'index.html', {"products": prs})


def new_products(request):
    return HttpResponse('New Products')


def old_product_page(request):
    return HttpResponse('Go to old product page')
