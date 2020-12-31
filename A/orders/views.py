from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem , Coupon , Contact
from cart.cart import Cart
from django.views.decorators.http import require_POST
from . forms import CouponForm,CouponForm , ContactForm
from django.utils import timezone
from django.contrib import messages

@login_required
def detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	form = CouponForm()
	return render(request, 'orders/order.html', {'order':order,'form':form})

@login_required
def order_create(request):
	cart = Cart(request)
	order = Order.objects.create(user=request.user)
	for item in cart:
		OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
	cart.clear()
	return redirect('orders:detail', order.id)


@require_POST
def coupon(request,order_id):
	now = timezone.now()
	form = CouponForm(request.POST)
	if form.is_valid():
		code = form.cleaned_data['code']
		try:
			coupon = Coupon.objects.get(code__iexact = code,valid_from__lte =now,valid_to__gte=now,active =True)
		except Coupon.DoesNotExist:
			messages.error(request,'This coupon does not exist','danger')
			return redirect('orders:detail',order_id)

		order = Order.objects.get(id=order_id)
		order.discount = coupon.discount
		order.save()
	return redirect('orders:detail',order_id)







def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sugest=Contact(email=cd['email'],full_name=cd['full_name'],body=cd['body'])
            sugest.save()
            messages.success(request,'you idea send successfully','success')
            return redirect('shop:home')


    else:
        form=ContactForm()



    


    return render(request,'orders/contact.html',{'form':form})


