"""coffee_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from coffee import views as cofee_Views
# from .views import coffee_list, create_coffee, coffee_detail, update_coffee, delete_coffee


urlpatterns = [
    path('admin/', admin.site.urls),
    path('coffee/', cofee_Views.coffee_list),
    path('coffee/create/', cofee_Views.create_coffee),
    path('coffees/<int:pk>/', cofee_Views.coffee_detail),
    path('coffees/<int:pk>/update/', cofee_Views.update_coffee),
    path('coffees/<int:pk>/delete/', cofee_Views.update_coffee),
]
