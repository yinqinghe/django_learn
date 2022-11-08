from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
# from reviews.views import
import os,sys

from django.conf.urls import  url
from . import  views
# app_name='app02'

router=DefaultRouter()
# router.register(r'product',Pro)
urlpatterns = [
    # path(r'login/', views.login,name='login'),
    # path(r'index/', views.index, name='index'),
    # path(r'book/', views.CourseView.as_view(), name='book'),
    url(r'add_book/',views.add_book,name='add_book'),
    url(r'show/',views.show,name='show'),
    url(r'edit_book/(\d+)/',views.edit_book,name='edit_book'),
    url(r'delete_book/(\d+)/',views.delete_book,name='delete_book'),
    # path(r'book/', views.noramal, name='book'),
    url(r'token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    url(r'token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),

]
