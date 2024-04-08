from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from bogis_nails.product.models import Product
from bogis_nails.cart.cart import Cart

@login_required
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantitues
    total_price = cart.total_price
    
    context = {
        'cart_products': cart_products,
        'quantities': quantities,
        'total_price': total_price,
    }
    
    return render(request, 'cart/cart_summary.html', context)


'''
Test the cart_add functionality:
    python manage.py shell 
    >>> from django.contrib.sessions.models import Session
    >>> k = Session.objects.get(pk='sz9jcpdbectt22pvgfhh9we7unu8cxad')
    >>> k.get_decoded()
    {
        'session_key': {'2': {'price': '21.99'}},
        '_auth_user_id': '29',
        '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
        '_auth_user_hash': 'a90e303e26d30a279ea8335bb93c242fef34d4fa3320b3ea0e1ed66f32feb095'
    }
'''

@login_required
def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        
        
        # Save the session
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity = cart.__len__()
        
        # response = JsonResponse({
        #     'Product Name': product.title,
        # })
        response = JsonResponse({
            'quantity': cart_quantity,
        })
        
        return response        


@login_required
def cart_update(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        
        # response = JsonResponse({
        #     'qty': product_qty,
        # })
        
        # return response
        return redirect('cart summary')


@login_required
def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)
        
        return redirect('cart summary')