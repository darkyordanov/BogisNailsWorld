from django.urls import include, path

from bogis_nails.catalog.views import \
    nails_catalog, nails_details , DeleteNailsView, CreateNailsDesignView, EditNailsDesignView

urlpatterns = (
    path('', nails_catalog, name='nails catalog'),
    path('add_nails_design_cbv/', CreateNailsDesignView.as_view(), name='add nails design cbv'),
    
    path('<int:pk>/', include([
        path('', nails_details, name='nails details'),
        path('edit_nails/', EditNailsDesignView.as_view(), name='edit nails'),
        path('delete_nails_cbv/', DeleteNailsView.as_view(), name='delete nails'),
    ])),
)
