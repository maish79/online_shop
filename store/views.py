from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.urls import reverse
# Create your views here.
 
def index(request):
    return HttpResponse('hi man')

def items(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'store/index.html', context)

def item_detail(request, id):
    item =Product.objects.get(id=id)
    context= {
        'item':item
    }

    return render(request, 'store/item-detail.html', context)