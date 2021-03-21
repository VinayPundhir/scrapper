"""scrapper URL Configuration

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
from django.urls import path,include
from . import views 

urlpatterns = [
    #hompage
 
    path('',views.home,name="home"),

    #search by name

    path('name/<str:name>',views.search,name="search"),

    # update redis database by calling using key

    path('update/<str:key>',views.download_today_data,name="download_today_data"),

    #download using the equity name

    path('download/<str:name>',views.download,name="download"),
]
