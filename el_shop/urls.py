"""el_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import MainpageView, ProductView, Product_updateView, Product_deleteView, Product_createView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainpageView.as_view(), name="product-list"),
    path('<int:pk>/product', ProductView.as_view(), name="product-view"),
    path('<int:pk>/update_product', Product_updateView.as_view(), name="product-update"),    
    path('<int:pk>/delete_product', Product_deleteView.as_view(), name="product-delete"),   
    path('create_product/', Product_createView.as_view(), name="product-add"),
]
