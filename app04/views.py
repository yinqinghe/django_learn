from django.shortcuts import render,HttpResponse
import uuid
import os
import json
from app03.models import *
from app04.models import *
from django.contrib.auth import authenticate,login,logout

from rest_framework.views import APIView
from rest_framework.response import Response
# 将序列化组件都放到一个单独的文件里面  然后引进来
from app03.serializer import BookSerializers_
# drf提供的认证失败的异常
from rest_framework.exceptions import AuthenticationFailed
from app04.service.permissions import *
from app04.service.throttles import *

from rest_framework.authentication import BaseAuthentication,SessionAuthentication
from app03.serializer import BookSerializers_,PublishSerializers,AuthorSerializers
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
# BrowsableAPIRenderer回复的数据自动给你生成一个页面形式的数据展示  一般开发的时候  都不用页面形式的
# JSONRenderer  回复的事json数据
# Create your views here.
from rest_framework.viewsets import ModelViewSet
# 引入分页
from rest_framework.pagination import PageNumberPagination
from app04.service.auth import *
from app04.service.serializer import *

class MyPagination(PageNumberPagination):   #分页组件
    page_size = 3   #每页数据显示条数
    page_query_param = 'pp'   #http://127.0.0.1/?pp=1   查询那一页的数据
    page_size_query_param = 'size'#如果显示的一页数据不够用的  想临时多看一些数据  可以通过这个参数访问http://127.0.0.1/?pp=1&size=5
    max_page_size = 10  #最大每页展示多少条
class AuthorView(ModelViewSet):
    renderer_classes = [JSONRenderer]   #响应器组件
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pagination_class = MyPagination
class UsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserAuth():
    # 每个认证类 都需要有个authenticate_header方法  并且有个参数request
    def authenticate_header(self,request):
        pass
    # authenticate方法固定的  并且必须有个参数  这个参数的新的request对象
    def authenticate(self,request):
        if request.method=="OPTIONS":
            return
        # token=request._request.GET.get("token")#这是老的request对象封装到了新的request对象中
        token=request.query_params.get('token')
        # 用户请求来了之后  我们获取token值  到数据库中验证
        usertoken=UserToken.objects.filter(token=token).first()
        print(usertoken)
        if usertoken:
            # 验证成功后  可以返回两个值  也可以什么都不返回
            return usertoken.user.user,usertoken.token
        else:
            # 因为源码内部进行了异常捕获  并且给你主动返回一个forbiden错误   这里主动抛出异常
            return AuthenticationFailed("认证失败")

        # if 1:
        ##这个方法返回两个值  并且这两个返回值封装到了新的request对象中了 request.user-->用户名
        # 和request.auth-->token值  这两个值作为认证结束后的返回结果
        #     return "user:jordan","auth:abcabc"
# 继承drf的BaseAuthentication类
class UserAuth1(BaseAuthentication):
    # 每个认证类 都需要有个authenticate_header方法  并且有个参数request
    # 继承了BaseAuthentication类之后  这个方法就不用写了
    # def authenticate_header(self,request):
    #     pass
    # authenticate方法固定的  并且必须有个参数  这个参数的新的request对象
    def authenticate(self,request):
        if request.method=="OPTIONS":
            return
        # token=request._request.GET.get("token")#这是老的request对象封装到了新的request对象中
        token=request.query_params.get('token')
        # 用户请求来了之后  我们获取token值  到数据库中验证
        usertoken=UserToken.objects.filter(token=token).first()
        print(usertoken)
        if usertoken:
            # 验证成功后  可以返回两个值  也可以什么都不返回
            return usertoken.user.user,usertoken.token
        else:
            # 因为源码内部进行了异常捕获  并且给你主动返回一个forbiden错误   这里主动抛出异常
            return AuthenticationFailed("认证失败")


class BookView(APIView):
    # 认证组件肯定是在get  post等方法之前执行的
    authentication_classes = [Authentication,]#认证类可以写多个  一个一个的顺序验证
    # permission_classes = [SVIPPermission,]
    # throttle_classes = [VisitThrottle1,]
    def get(self,request):
        # 查看所有书籍
        # 这样就拿到了上面UserAuth类的authenticate方法的两个返回值
        print('request.user',request.user.user)
        print('request.auth',request.auth)
        book_obj_list=Book.objects.all()
        pnb=MyPagination()
        paged_book_list=pnb.paginate_queryset(book_obj_list,request)

        # s_books=BookSerializers_(book_obj_list,many=True)
        s_books=BookSerializers_(paged_book_list,many=True,context={'request':request})

        print(s_books)
        return Response({'all_bookings':s_books.data})
        # return HttpResponse(s_books.data)

class LoginView(APIView):
    def post(self,request):


        res={'code':1,'msg':None,'user':None,'token':None}
        print(request.data)

        try:
            user=request.data.get('user')
            pwd=request.data.get('pwd')
            print(user)
            # 数据库中查询
            user_obj=User.objects.filter(user=user,pwd=pwd).first()
            # user_obj = authenticate(username=user, password=pwd)
            print(user_obj)

            if user_obj:
                res['user']=user_obj.user
                # login(request, user_obj)
                request.session['user_id']=user_obj.user
                random_str=uuid.uuid4()
                # random_str=os.urandom(16)
                UserToken.objects.update_or_create(
                    user=user_obj,
                    defaults={'token':random_str,},
                    expire_time='2022-11-12 11:25:45',
                )
                res['token']=random_str
                res['msg']='登录成功'
            else:
                res['code']=0
                res['msg']='用户名或密码错误'

        except Exception as e:
            res['code']=2
            res['msg']=str(e)
        return Response(res)

