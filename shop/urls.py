from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.products_all, name='products_all'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('sobrenosotros/', views.sobrenosotros, name='sobrenosotros'),
]