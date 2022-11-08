from django.urls import path, include
import os,sys

from django.conf.urls import  url
from . import  views
# app_name='app02'
from rest_framework import routers

router=routers.DefaultRouter()
# 自动生成两个URL
router.register(r'authors',views.AuthorView)  #url注册器

urlpatterns = [
    # GET和POST接口的URL
    path(r'book/', views.BookView.as_view(), name='book'),
    # PUT，DELETE，GET请求接口
    # path(r'book/(?<id>\d+)/', views.SBookView.as_view()),
    path(r'book/<int:id>/', views.SBookView.as_view()),
    # path(r'book/(\d+)/', views.SBookView.as_view()),
    url(r'^publishs/', views.PublishView.as_view()),

    url(r'^publishs/(?P<pk>\d+)/',views.SPublishView.as_view()),
    # url(r'^publishs/<int:pk>/', views.SPublishView.as_view()),

    # url(r'',include(router.urls)),
    url(r'^authors/$',views.AuthorView.as_view({"get":"list","post":"create"}),),
    url(r'authors/(?P<age>\d+)',views.AuthorView.as_view({
        'get':'retrieve',
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy',
    }))

]