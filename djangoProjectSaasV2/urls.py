"""
URL configuration for djangoProjectSaasV2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from djangoProjectSaasV2 import views
from my_auth import views as auth_views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", auth_views.login_view, name="login_view"),
    path("about/", views.about_page_view, name="about"),
    path("admin/", admin.site.urls),
]
