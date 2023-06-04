from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from app_sportbar.models import MenuPosition
from .cart import Cart
from .forms import CartAddProductForm, OrderForm
from django.http import JsonResponse
from decimal import Decimal
from django.views.generic import View, ListView
from .models import Order, OrderItem


@require_POST
def cart_add(request, product_id):
    cart_instance = Cart(request)
    product = get_object_or_404(MenuPosition, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        quantity=form_data['quantity']
        cart_instance.add(product=product,
                 quantity=quantity,
                 update_quantity=form_data['update'])
        
    # editing cart from cart/detail.html  with product quantity   
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'newTotalProductPrice':Decimal(cart_instance.cart[str(product_id)]['price'])*quantity,
            'newTotal':cart_instance.get_total_cost(),
            'product_id':product_id,
            'newQuantity':quantity})
       
    
    else:
        return redirect(request.META.get('HTTP_REFERER'))

# remove from cart
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(MenuPosition, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

# display cart with goods
def cart_detail(request):
    cart_instance = Cart(request)
    form = CartAddProductForm()
    return render(request, 'cart/cart.html', {'cart_instance': cart_instance, 'cart_form':form})
    
def is_cart(request):
    cart_instance = Cart(request)
    if len(cart_instance) > 0:
        return JsonResponse({'response':'yes', 'goodsNumber':len(cart_instance)})
    else:
        return JsonResponse({'response':'no'})

class   CreateOrder(View):
    def get(self, request):
        orderForm = OrderForm()
        return render(request, 'cart/order_form.html', {'order_form':orderForm})
    
    def post(self, request):
        order_form = OrderForm(request.POST)
        cart_instance = Cart(request)
        if order_form.is_valid():
            if len(cart_instance) > 0:
                if request.user.is_authenticated:
                    order = order_form.save(commit=False)
                    order.client = request.user
                    order.save()
                else:
                    order = order_form.save()
            for item in cart_instance:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart_instance.clear()
            return JsonResponse({'response':'success'})           
        else:
            return JsonResponse({'response':'validation error'})

class OrdersList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)
   