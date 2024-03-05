from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, ListView

from bogis_nails.catalog.forms import NailDesignCreateForm, NailDesignEditForm, NailDesignDeleteForm
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


def nails_details(request, pk):
    nails_design = NailDesign.objects.get(id=pk)
    
    context = {
        'nails_design': nails_design
    }
    
    return render(request, 'catalog/nails_details.html', context)


# CBV's
class CreateNailsDesignView(CreateView):
    model = NailDesign
    form_class = NailDesignCreateForm
    template_name = 'catalog/add_nails_design.html'

    def get_success_url(self):
        return reverse_lazy('nails details', kwargs={
            'pk': self.object.pk
        })

# FBV's
# def add_nails_design(request):
#     if request.method == 'POST':
#         form = NailDesignCreateForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             nails_design = form.save()
#             return redirect('nails catalog')
#     else:
#         form = NailDesignCreateForm()
        
#     context = {
#         'form': form,
#     }
        
#     return render(request, 'catalog/add_nails_design.html', context)


# CBV's
class EditNailsDesignView(UpdateView):
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
    

# FBV's
# def edit_nails(request, pk):
#     # Get the instance of NailDesign with the given primary key
#     nails_design = NailDesign.objects.get(id=pk)
    
#     # Create an instance of the form with the instance of NailDesign
#     form = NailDesignEditForm(request.POST or None, instance=nails_design)
    
#     if request.method == 'POST':  # Check if the request method is POST
#         if form.is_valid():
#             form.save()
#             # Redirect to the appropriate URL after successful form submission
#             return redirect('nails details', pk=pk)
    
#     # Prepare the context dictionary to pass data to the template
#     context = {
#         'form': form,
#         'nails_design': nails_design,
#     }
    
#     # Render the template with the provided context
#     return render(request, 'catalog/edit_nails.html', context)


# CBV's
class DeleteNailsView(DeleteView):
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


# FBV's
# def delete_nails(request, pk):
#     nails_design = NailDesign.objects.get(id=pk)
    
#     form = NailDesignDeleteForm(request.POST or None, instance=nails_design)
    
#     if request.method == 'POST':
#         form.save()
#         return redirect('nails catalog')
        
#     context = {
#         'form': form,
#         'nails_design': nails_design,
#     }
        
#     return render(request, 'catalog/delete_nails.html', context)


class NailDesignSearchListView(ListView):
    model = NailDesign
    template_name = ".html"

    def get_success_url(self):
        return reverse_lazy('nails catalog', kwargs={
            'pk': self.object.pk,
            'color': self.object.color,
            'size': self.object.size,
        })
