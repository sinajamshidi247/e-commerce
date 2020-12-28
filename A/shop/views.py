from django.shortcuts import render , get_object_or_404
from.models import Product , Categories
from cart.forms import CartAddForm


def Home(request,slug=None):
    products = Product.objects.filter(available=True)
    categories = Categories.objects.filter(is_sub=False) #اونایی که دسته بندی ندارن رو بگیره فقط 
    if slug:
        category = get_object_or_404(Categories,slug=slug)
        products = products.filter(category=category)

    return render(request,'shop/home.html',{'products':products,'categories': categories})




def product_detail(request, slug):
    product = get_object_or_404(Product , slug = slug)
    form=CartAddForm()
    return render(request , 'shop/product_detail.html' ,{'product':product,'form':form})
