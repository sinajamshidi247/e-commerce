from django.shortcuts import render , get_object_or_404,redirect
from.models import Product , Categories , Comment
from cart.forms import CartAddForm
from django.contrib import messages 
from .forms import AddReplyForm
from django.contrib.auth.decorators import login_required


def Home(request,slug=None):
    products = Product.objects.filter(available=True)
    categories = Categories.objects.filter(is_sub=False) #اونایی که دسته بندی ندارن رو بگیره فقط 
    if slug:
        category = get_object_or_404(Categories,slug=slug)
        products = products.filter(category=category)

    return render(request,'shop/home.html',{'products':products,'categories': categories})




def product_detail(request, slug):
    product_all = get_object_or_404(Product , slug = slug)
    form_one=CartAddForm()
    product=get_object_or_404(Product,slug=slug)
    comments =Comment.objects.filter(product=product)
    if request.method == "POST":
        form=AddReplyForm(request.POST)
        if  form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.product=product
            new_comment.user=request.user
            new_comment.save()
            messages.success(request,'your reply submitted successfully','success')
    else:
        form = AddReplyForm()
    return render(request , 'shop/product_detail.html' ,{'product':product_all,'form_one':form_one,'form':form,'comments':comments})




