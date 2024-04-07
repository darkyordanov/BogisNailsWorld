from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from bogis_nails.product.models import Product
from bogis_nails.cart.cart import Cart


def cart_summary(request):
    context = {
        
    }
    
    return render(request, 'cart/cart_summary.html', context)


def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        
        # Save the session
        cart.add(product=product)
        
        response = JsonResponse({
            'Product Name': product.title,
        })
        
        return response        


def cart_delete(request):
    pass


def cart_update(request):
    pass
