from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from bogis_nails.product.models import Product
from bogis_nails.cart.cart import Cart


def cart_summary(request):
    context = {
        
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
