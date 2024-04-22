"""
URL configuration for firstweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings  
from django.conf.urls.static import static

from myapp import views
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.first),
    path('contact',views.second),
    path('login',views.third),
    path('data',views.storedata),
    path('sign',views.sign),
    path('signupdata',views.signindata),
    path('shop',views.shopnow),
    path('blog',views.blogg),
    path('pet',views.pett),
    path('logindata',views.lgdata),
    path('cart',views.cart),
    path('cartpass',views.cartpass),
    path('deletcart',views.deletcart),
    path('plus',views.plus),
    path('minus',views.minus),
    path('js',views.js),

] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)