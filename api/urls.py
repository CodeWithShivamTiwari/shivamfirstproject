from django.urls import path
from .import views

urlpatterns = [

    path('product-list/', views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>', views.ViewProduct, name='product-detail'),
    path('product-Create/', views.CreateProduct, name='product-Create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),
    
]


