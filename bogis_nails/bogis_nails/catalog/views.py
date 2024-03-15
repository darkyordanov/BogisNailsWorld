from django.db.models.base import Model as Model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView

from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth.decorators import login_required

from bogis_nails.catalog.forms import \
    NailDesignCreateForm, NailDesignEditForm
    
from bogis_nails.catalog.models import NailDesign


def nails_catalog(request):
    # Retrieve all nail designs initially
    nail_designs = NailDesign.objects.all()

    # Fetch distinct colors and sizes
    colors = NailDesign.objects.values_list('colors', flat=True).distinct()
    sizes = NailDesign.objects.values_list('size', flat=True).distinct()

    # Handle search functionality
    if request.method == 'GET':
        color = request.GET.get('color')
        size = request.GET.get('size')
        
        if color:
            nail_designs = nail_designs.filter(colors=color)
        if size:
            nail_designs = nail_designs.filter(size=size)

    context = {
        'nail_designs': nail_designs,
        'colors': colors,
        'sizes': sizes,
    }

    return render(request, 'catalog/nails_catalog.html', context)


@login_required
def nails_details(request, pk):
    nails_design = NailDesign.objects.get(id=pk)
    
    context = {
        'nails_design': nails_design
    }
    
    return render(request, 'catalog/nails_details.html', context)


class CreateNailsDesignView(auth_mixin.LoginRequiredMixin, CreateView):
    model = NailDesign
    form_class = NailDesignCreateForm
    template_name = 'catalog/add_nails_design.html'

    def get_success_url(self):
        return reverse_lazy('nails details', kwargs={
            'pk': self.object.pk
        })


class EditNailsDesignView(auth_mixin.LoginRequiredMixin, UpdateView):
    model = NailDesign
    form_class = NailDesignEditForm
    template_name = 'catalog/edit_nails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nails_design'] = self.get_object()
        return context

    def get_success_url(self):
        return reverse_lazy('nails details', kwargs={
            'pk': self.object.pk
        })
    

class DeleteNailsView(auth_mixin.LoginRequiredMixin, DeleteView):
    model = NailDesign
    template_name = "catalog/delete_nails.html"
    # if I uncomment the form_class , the delete func doesn't work success
    # form_class = NailDesignDeleteForm
    success_url = reverse_lazy('nails catalog')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nails_design'] = self.get_object()
        return context
    
    def delete(self, request, *args, **kwargs):
        # Delete object and redirect to success URL
        self.object = self.get_object()
        self.object.delete()
        return super().delete(request, *args, **kwargs)
