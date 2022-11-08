from django.conf.urls import  url
from . import  views
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
urlpatterns = [

    # path(r'book/(\d+)/', views.SBookView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),

    url(r'^books/$', views.BookView.as_view()),
    url(r'^authors/$', cache_page(30)(views.AuthorView.as_view({"get":"list","post":"create"}))),
    url(r'^users/$', views.UsersView.as_view({"get": "list", "post": "create"})),

    url(r'users/(?P<pk>\d+)', cache_page(20)(views.UsersView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }))),
    # url(r'^publishs/<int:pk>/', views.SPublishView.as_view()),
]