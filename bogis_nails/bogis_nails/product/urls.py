from django.urls import include, path

from bogis_nails.product.views import \
    ProductsView, DetailsProductView, AddProductView, EditProductView, DeleteProductView

urlpatterns = (
    path('', ProductsView.as_view(), name='products'),
    path('add_product/', AddProductView.as_view(), name='add product'),
    
    path('<int:pk>/', include([
        path('', DetailsProductView.as_view(), name='details product'),
        path('edit_products/', EditProductView.as_view(), name='edit product'),
        path('delete_product/', DeleteProductView.as_view(), name='delete product'),
    ])),
    # path('add-to-cart/<int:pk>/', add_to_cart, name='add to cart'),
)