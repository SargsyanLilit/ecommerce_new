from django.urls import path, include
from products import views


urlpatterns = [
    path('', views.home, name='home'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('general/', views.general, name='general'),
    path('product-view/<int:product_id>/', views.product_view, name='product-view'),
    path('search/', views.SearchProductsView.as_view(), name='search-results'),
]