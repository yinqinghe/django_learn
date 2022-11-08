from django.shortcuts import render
from app03.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from rest_framework.viewsets import ModelViewSet

from app03.serializer import *
from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
# ListModelMixin查看所有数据  对应着咱们上面的get查看所有数据的接口
# CreateModelMixin添加数据的操作  封装了create操作  对应着POST添加数据的接口
# UpdateModelMixin更新
# DestroyModelMixin销毁（删除）
# RetrieveModelMixin获取单条数据

from django_filters import rest_framework
from rest_framework import filters
import django_filters
from django_filters import rest_framework


# Create your views here.



class PublishView(ListModelMixin,CreateModelMixin,generics.GenericAPIView):

    # 下面这两个变量和对应数据是必须给的
    queryset = Publish.objects.all()
    serializer_class = PublishSerializers
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filterset_class=PublishSerializers_f
    def get(self,request):

        return self.list(request)
    def post(self,request):

        return self.create(request)
    # filterset_fields=('city','email')

    # search_fields=('city','email')
    # ordering_fields=('book','nid')
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
class PublishView1(ListModelMixin,CreateModelMixin,generics.GenericAPIView):

    # 下面这两个变量和对应数据是必须给的
    queryset = Publish.objects.all()
    serializer_class = PublishSerializers
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class=PublishSerializers_f
    # def get_queryset(self):
    #     keyword=self.request.query_params.get('city')
    #     print(keyword)
    #     if not keyword:
    #         queryset=Publish.objects.all()
    #     else:
    #         queryset=Publish.objects.filter(city=keyword)
    #     return queryset
    def get(self,request):

        return self.list(request)
    def post(self,request):

        return self.create(request)

class SPublishView(UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,generics.GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializers
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class=PublishSerializers_f
    # def get_queryset(self):
    #     keyword=self.request.query_params.get('city')
    #     print(keyword)
    #     if not keyword:
    #         queryset=Publish.objects.all()
    #     else:
    #         queryset=Publish.objects.filter(city=keyword)
    #     return queryset
    def get(self,request,*args,**kwargs):  #*args,**kwargs是为了接受URL的哪些参数的，自己写的pk参数
        print(*args)
        # print(**kwargs)
        print('get')
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# ListCreateAPIView类封装了get和create方法
# class AuthorView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers

# RetriveUpdateDestroyAPIView这个类封装了put,get,patch,delete方法
class SAuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    filterset_class=AuthorFilter
    lookup_field = 'age'



class BookSerializers(serializers.Serializer):
    class Meta:
        model=Book
        fields="__all__"
    title=serializers.CharField(max_length=32)
    price=serializers.DecimalField(max_digits=5,decimal_places=2)

    #一对多处理
    publish_email=serializers.CharField(max_length=32,source='publish.email')
    publish_name=serializers.CharField(max_length=32,source='publish.name')

    #多对多的处理
    authors=serializers.SerializerMethodField()  #这是多对多的关系
    #下面的函数名必须是get_字段名
    def get_authors(self,obj):

        author_list_values=[]
        author_dict={}
        author_list=obj.authors.all()
        for i in author_list:
            author_dict['id']=i.pk
            author_dict['name']=i.name
            author_list_values.append(author_dict)
        return author_list_values

# 如果有上百张表   这是一种比较简单的方式
class BookSerializerser(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
        # 要把下面注释掉  不然get和post请求我们用的都是这个序列化组件  会出现对多对变量冲突的问题
        # 所以一般都将读操作和写操作分成两个序列化组件来写
    # authors=serializers.SerializerMethodField()  #这是多对多的关系
        #下面的函数名必须是get_字段名
    def get_authors(self,obj):

        author_list_values=[]
        author_dict={}
        author_list=obj.authors.all()
        for i in author_list:
            author_dict['id']=i.pk
            author_dict['name']=i.name
            author_list_values.append(author_dict)
        return author_list_values
    # publish_name=serializers.CharField(max_length=32,source='publish.name')
    #如果序列化后有个数据不想要它   可以起个相同的变量名来覆盖它
    # publish=serializers.CharField(max_length=32,source='publish.name')

# 一个读序列化组件  一个写序列化组件
class BookSerializers1(serializers.ModelSerializer):
    class Metaa:
        model=Book
        fields="__all__"
    def create(self, validated_data):
        print(validated_data)

        authors=validated_data.pop('authors')
        obj=Book.objects.create(**validated_data)
        obj.authors.add(*authors)
        return obj

class BookSerializers2(serializers.ModelSerializer):
    class Meta:
        model=Book
        fiedls="__all__"
    authors=serializers.SerializerMethodField()
    def get_authors(self,obj):
        print('get_auhtor')
        author_list_values=[]
        author_dict={}
        author_list=obj.authors.all()
        for i in author_list:
            author_dict['id']=i.pk
            author_dict['name']=i.name
            author_list_values.append(author_dict)

        return author_list_values
    publish=serializers.CharField(max_length=32,source='publish.name')



class BookSerializers10(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class BookView(APIView):
    def get(self,request):
        # 查看所有书籍
        book_obj_list=Book.objects.all()
        s_books=BookSerializerser(book_obj_list,many=True)
        return Response(s_books.data)

    def post(self,request):
        # 添加一条数据
        b_serializer=BookSerializerser(data=request.data,many=False)
        print(b_serializer.is_valid())    #验证插入的一条数据是否完整
        if b_serializer.is_valid():
            print('isvalid')
            b_serializer.save()
            return Response(b_serializer.data)
        else:
            return Response(b_serializer.errors)

        pass

class SBookView(APIView):
    def get(self,request,id=1):
        # 获取单条数据
        print(id)
        book_obj=Book.objects.get(pk=id)
        book_serializer=BookSerializers10(book_obj,many=False)
        return Response(book_serializer.data)
    def put(self,request,id):
        # 更新一条数据
        print('put',id)
        book_obj=Book.objects.get(pk=id)
        b_s=BookSerializers10(data=request.data,instance=book_obj,many=False)
        # 要写insance  由于我们使用的ModelSerializer  前段提交过来的数据必须是所有字段的数据   id字段不用

        if b_s.is_valid():
            b_s.save()
            return Response(b_s.data)
        else:
            return Response(b_s.errors)

    def delete(self,request,id):
        # 删除一条数据
        book_obj=Book.objects.get(pk=id).delete()
        return Response("")    #接口规范说最好返回一个空