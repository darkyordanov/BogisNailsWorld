from bogis_nails.product.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # Get current key session if it exist
        cart = self.session.get('session_key')
        
        # If the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # Make sure cart is available on all pages of site
        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        if product_id in self.cart:
            pass
        
        else:
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
    def __len__(self):
        return len(self.cart)
        
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        return products
    
    def get_quantitues(self):
        quantities = self.cart
        
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        ourcart = self.cart
        # Update dictionary of cart
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        
        return self.cart
    
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
        
    def total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        result = 0
        
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        result = result + (product.sale_price * value)
                    else:
                        result = result + (product.price * value)
        
        return result