from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Product_list,name="ProductList"),
    path('<int:prodId>/',views.Single_Product,name="Single_Product"),
]