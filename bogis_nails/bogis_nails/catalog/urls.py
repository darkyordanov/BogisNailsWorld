from django.urls import include, path

from bogis_nails.catalog.views import \
    nails_catalog, DetailsNailsDesignView, CreateNailsDesignView, EditNailsDesignView, DeleteNailsView

urlpatterns = (
    path('', nails_catalog, name='nails catalog'),
    path('add_nails_design/', CreateNailsDesignView.as_view(), name='add nails design'),
    
    path('<int:pk>/', include([
        path('', DetailsNailsDesignView.as_view(), name='nails details'),
        path('edit_nails/', EditNailsDesignView.as_view(), name='edit nails'),
        path('delete_nails/', DeleteNailsView.as_view(), name='delete nails'),
    ])),
)