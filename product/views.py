from django.shortcuts import render
from .models import Product_list,Product_detail
# Create your views here.


def product_list(request):
    goods = Product_list.objects.all().order_by("pk")
    products = Product_detail.objects.all().order_by("pk")
    print(goods)
    return render(
        request,"product/product_list.html",
        {
            'goods' : goods ,
            'products': products
        }
    )