from django.contrib import admin
from django.urls import path,include
from . import  views

from django.conf.urls import  url

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^articles/$',views.Articles.as_view()),
    url(r'^article/$',views.ArticleList.as_view()),
    url(r'^article/(?P<pk>\d+)/$', views.ArticleDetail.as_view()),
    url(r'api-auth/',include('rest_framework.urls'))

]