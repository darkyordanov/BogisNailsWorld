from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bogis_nails.product.models import Product

from bogis_nails.product.forms import ProductForm


class ProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/products.html'
    

class DetailsProductView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/details_product.html'
    

class AddProductView(CreateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/add_product.html'

    def get_success_url(self) -> str:
       return reverse_lazy('details product', kwargs={
           'pk': self.object.pk
       })
            

class EditProductView(UpdateView):
    pass


class DeleteProductView(DeleteView):
    pass

