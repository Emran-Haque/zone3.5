
from django.urls import path
from . import views
from store.api import views as api_views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),


    path('api/products/', api_views.product_list, name='api_product_list'),
    path('api/products/<slug:slug>/', api_views.product_detail, name='api_product_detail'),

]