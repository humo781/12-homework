from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('about_page/', views.about_page, name='about'),
    path('product_list/', views.products_list, name='list'),
    path('product_detail/<int:pk>/', views.product_detail, name='detail'),
    path('product_create/', views.product_create, name='create'),
]
