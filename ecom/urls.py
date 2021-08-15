"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('Csignup/', views.Csignup, name='Csignup'),
    path('Clogin/', views.Clogin, name='Clogin'),
    path('selsignup/', views.selsignup, name='selsignup'),
    path('selsignin/', views.selsignin, name='selsignin'),
    path('cart/', views.cart, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('productdetail/', views.productdetail, name='productdetail'),
    path('products/', views.products, name='products'),
    path('mainpro/', views.mainpro, name='mainpro'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('displaycart/', views.displaycart, name='displaycart'),
    path('removefromcart/', views.removefromcart, name='removefromcart'),
    path('logout/', views.logout, name='log'),

    path('blackbox/', views.blackbox, name='blackbox'),
    path('glitterbottle/', views.glitterbottle, name='glitterbottle'),
    path('heartframe/', views.heartframe, name='heartframe'),
    path('wallhanging/', views.wallhanging, name='wallhanging'),
    path('kitkatcake/', views.kitkatcake, name='kitkatcake'),
    path('clock/', views.clock, name='clock'),
    path('teddy/', views.teddy, name='teddy'),
    path('photoframe/', views.photoframe, name='photoframe'),
    path('chocolatecake/', views.chocolatecake, name='chocolatecake'),
    path('cups/', views.cups, name='cups'),

    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('aditem/', views.aditem, name='aditem'),
    path('confirmorder/', views.confirmorder, name='confirmorder'),
    path('myorders/', views.myorders, name='myorders'),
    path('myprof/', views.myprof, name='myprof'),
    path('pickup/', views.pickup, name='pickup'),
    path('thank/', views.thank, name='thank'),
    path('nocart/', views.nocart, name='nocart'),
    path('seller/', views.seller, name='seller'),
    path('farmlogin/', views.farmlogin, name='farmlogin'),
    path('consumerlogin/', views.consumerlogin, name='consumerlogin'),
    path('confirmorder/', views.confirmorder, name='confirmorder'),
    path('myorders/', views.myorders, name='myorders'),
    path('razor/', views.razor, name='razor'),
    path('success/', views.success, name='success'),
]
