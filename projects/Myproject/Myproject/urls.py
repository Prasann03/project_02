"""
URL configuration for Myproject project.

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
from django.urls import path, include
from django.conf import settings
from . import index

urlpatterns = [
    path('',index.home,name='home'),
    path('Disclaimer',index.Disclaimer,name='Disclaimer'),
    path('searching',index.searching,name='searching'),
    path('info',index.info,name='info'),
    path('successful_profile',index.successful_profile,name='successful_profile'),
    path('loginsuccess',index.loginsuccess,name='loginsuccess'),
    path('signup',index.signup,name='signup'),
    path('App_page',index.App_page,name='App_page'),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    
]
