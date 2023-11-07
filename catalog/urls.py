from django.urls import path

from catalog.views import ProductListView, ContactDetailView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView

app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactDetailView.as_view(), name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<str:name>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<str:name>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<str:name>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/version/create/', VersionCreateView.as_view(), name='version_create'),

]
