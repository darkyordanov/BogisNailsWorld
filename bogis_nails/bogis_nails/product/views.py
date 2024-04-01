from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView
    
from bogis_nails.product.models import Product
from bogis_nails.product.forms import ProductForm

# from django.contrib.auth.mixins import PermissionRequiredMixin


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Product, Cart


class ProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/products.html'
    

class DetailsProductView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/details_product.html'
    

class AddProductView(auth_mixin.LoginRequiredMixin, CreateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/add_product.html'

    def get_success_url(self):
       return reverse_lazy('details product', kwargs={
           'pk': self.object.pk
       })
            

class EditProductView(auth_mixin.LoginRequiredMixin, UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/edit_products.html'
    
    def get_success_url(self):
        return reverse_lazy('details product', kwargs={
            'pk': self.object.pk
        })


class DeleteProductView(auth_mixin.LoginRequiredMixin, DeleteView):
    queryset = Product.objects.all()
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('products')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return super().delete(request, *args, **kwargs)
    

# def add_to_cart(request, pk):
#     # Retrieve the product based on the primary key
#     product = get_object_or_404(Product, pk=pk)
    
#     # Check if a cart exists for the user, if not create one
#     if not request.session.get('cart_id'):
#         cart = Cart.objects.create()
#         request.session['cart_id'] = cart.id
    
#     cart_id = request.session.get('cart_id')
#     cart = Cart.objects.get(id=cart_id)
    
#     # Add the product to the cart
#     cart.products.add(product)
    
#     # Optionally, you can add a success message
#     messages.success(request, f"{product.title} added to cart.")
    
#     # Redirect to the same page or wherever you want
#     return redirect('name_of_the_same_page_or_cart_page')