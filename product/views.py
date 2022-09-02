from django.shortcuts import render
from .models import Product_list
# Create your views here.


def product_list(request):
    goods = Product_list.objects.all().order_by("pk")
    print(goods)
    return render(
        request,"product/product_list.html",
        {
            'goods' : goods 
        }
    )