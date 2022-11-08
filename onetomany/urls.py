from django.urls import path
import os,sys

from django.conf.urls import  url
from . import  views
# app_name='app02'
urlpatterns = [
    # GET和POST接口的URL
    path(r'book/', views.BookView.as_view(), name='book'),
    # PUT，DELETE，GET请求接口
    path(r'book/(?<id>\d+)/', views.SBookView.as_view()),

]