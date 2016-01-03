"""NFCow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin

# from branches.views import BranchDetailView
from branches.views import BranchListView
from products.views import product_detail
from rel_products_branches.views import ProductInBranchListView
from shopping_carts.views import ShoppingCartListView, cancel_shopping_cart
from rel_products_shopping_carts.views import product_remove
from orders.views import OrderDetailView, OrderListView


urlpatterns = [
    # url(r'^branches/(?P<pk>[\d]+)', BranchDetailView.as_view()),
    url(r'^branches/([\d]+)', BranchListView.as_view(), name='product-list'),
    url(r'^products/(?P<id>[\d]+)', product_detail, name='product-detail'),
    url(r'^menu/([\d]+)', ProductInBranchListView.as_view(), name='branch-menu'),
    url(r'^shopping-cart/([\d]+)', ShoppingCartListView.as_view(), name='shopping-cart'),
    url(r'^shopping-cart-cancel/', cancel_shopping_cart, name='shopping-cart-cancel'),    
    url(r'^shopping-cart-remove/(?P<id>[\d]+)/(?P<sc>[\d]+)', product_remove, name='shopping-cart-remove-product'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT, }),
    url(r'^orders/', OrderListView.as_view(), name='orders-list'),    
    url(r'^order-detail/(?P<pk>[\d]+)', OrderDetailView.as_view(), name='order-detail'),    
    url(r'^admin/', admin.site.urls),
]