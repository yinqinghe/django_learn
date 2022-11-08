"""bms URL Configuration

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
import os,sys

from django.conf.urls import  url
from . import  views
# app_name='app01'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.book_list),
    path(r'pub_list/',views.publisher_list),
    path(r'add_pub/', views.add_publisher),
    path(r'author_list/',views.author_list),
    path(r'add_author/', views.add_author,name='add_author'),
    path(r'drop_author/', views.drop_author),
    path(r'edit_author/', views.edit_author,name='edit_author'),

    path(r'book_list/', views.book_list),
    path(r'add_book/', views.add_book),
    path(r'drop_book/', views.drop_book),
    path(r'edit_book/', views.edit_book),

    path(r'login/', views.logins,name='login'),
    # path(r'accounts/login/', views.logins, name='login'),

    # path(r'^signup/', views.signup),
    path(r'register/', views.register,name='register'),
    path(r'logout/', views.logoutd,name='logout'),
    path(r'time_op/', views.time_op, name='time_op'),
    path(r'index/', views.index, name='index'),
    path(r'set_password/', views.set_password, name='set_password'),

    url(r'more_database/',views.more_database)
]
