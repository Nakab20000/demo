from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product1.html/', views.product_html1, name='product_html1'),
    path('product2.html/', views.product_html2, name='product_html2'),
    path('product3.html/', views.product_html3, name='product_html3'),
]
