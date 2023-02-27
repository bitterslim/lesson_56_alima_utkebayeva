from django.urls import path

from webapp.views.index import index_view
from webapp.views.product import detail_view, add_product, update_view, delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('products', index_view, name='index'),
    path('products/<int:pk>', detail_view, name='product_detail'),
    path('products/add', add_product, name='product_add'),
    path('products/<int:pk>/update', update_view, name='product_update'),
    path('products/<int:pk>/delete', delete_view, name='product_delete')

]
