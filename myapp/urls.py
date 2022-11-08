from django.urls import path
import os,sys

from django.conf.urls import  url
from . import  views
# app_name='app02'
urlpatterns = [
    # GET和POST接口的URL
    # path(r'book/(?<id>\d+)/', views.urls, name='book'),
    # PUT，DELETE，GET请求接口
    path(r'book/<int:id>/', views.urls),

]