from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views import generic as views

from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from bogis_nails.catalog.forms import \
    NailDesignCreateForm, NailDesignEditForm
    
from bogis_nails.catalog.models import Collection, NailDesign


def nails_catalog(request):
    nail_designs = NailDesign.objects.all().order_by('-created_at')

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
    
    # Pagination
    paginator = Paginator(nail_designs.all(), 18)
    page_number = request.GET.get('page')
    nail_designs = paginator.get_page(page_number)

    context = {
        'collection_data': nail_designs,
        'colors': colors,
        'sizes': sizes,
    }

    return render(request, 'catalog/nails_catalog.html', context)


class DetailsNailsDesignView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DetailView):
    permission_required = [
        'catalog.view_naildesign'
    ]
    queryset = NailDesign.objects.all()
    template_name = 'catalog/nails_details.html'
    


class CreateNailsDesignView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
    permission_required = 'catalog.add_naildesign'
    form_class = NailDesignCreateForm
    template_name = 'catalog/add_nails_design.html'

    def get_success_url(self):
        return reverse_lazy('nails details', kwargs={
            'pk': self.object.pk
        })


class EditNailsDesignView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.UpdateView):
    permission_required = 'catalog.change_naildesign'
    queryset = NailDesign.objects.all()
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
    

class DeleteNailsView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DeleteView):
    permission_required = 'catalog.delete_naildesign'
    queryset = NailDesign.objects.all()
    template_name = "catalog/delete_nails.html"
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
    
    
@login_required
def collection(request):
    collection_list, created = Collection.objects.get_or_create(user=request.user)
    
    # Pagination
    paginator = Paginator(collection_list.nails_designs.all(), 12)
    page_number = request.GET.get('page')
    collection_data = paginator.get_page(page_number)
    
    context = {
         'collection_data': collection_data,
    }
    
    return render(request, 'catalog/collection.html', context)


@login_required
def add_to_collection(request, nails_design_id):
    user = request.user
    nails_design = get_object_or_404(NailDesign, id=nails_design_id)
    
    # Get the user's collection if it exists
    collection = Collection.objects.filter(user=user).first()
    
    if collection:
        collection.nails_designs.add(nails_design)
        
        nails_design.save()
        
    return redirect('nails catalog')

    
@login_required
def remove_from_collection(request):
    if request.method == 'POST' and request.POST.get('action') == 'post':
        nails_design_id_str = request.POST.get('nails_design_id')
        
        if nails_design_id_str is not None and nails_design_id_str.isdigit():
            nails_design_id = int(nails_design_id_str)
            collection = get_object_or_404(Collection, user=request.user)
            nail_design = get_object_or_404(NailDesign, id=nails_design_id)
            
            collection.nails_designs.remove(nail_design)
            
    return redirect('collection')

