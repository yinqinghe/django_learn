from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from app02.models import *
import json
from rest_framework.views import APIView

# 导入解析器
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
# JSONParser：解析json数据的
# FormParser：解析urlencoded数据的
# MultiPartParser：解析文件数据的

from rest_framework.response import Response
from rest_framework import status,serializers
from django.core.serializers import serialize  #django的序列化组件 不是drf的序列化组件

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie,vary_on_headers
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_extensions.cache.mixins import ListCacheResponseMixin,RetrieveCacheResponseMixin,CacheResponseMixin
from utils.form import *
def edit_book(request,n):
    return HttpResponse('编辑页面')
def delete_book(request,n):
    return HttpResponse('删除页面')
def add_book(request,n=1):
    book_obj=Book.objects.filter(pk=n).first()
    if request.method=='GET':
        form_obj=BookForm()
        return render(request,'book_add.html',{'form_obj':form_obj})
    else:
        print(request.POST)
        form_obj=BookForm(request.POST)
        print(form_obj.is_valid())
        print(form_obj.errors)
        if form_obj.is_valid():
            print(form_obj.cleaned_data)
            authors_obj=form_obj.cleaned_data.pop('authors')
            new_book_obj=Book.objects.create(**form_obj.cleaned_data)
            new_book_obj.authors.add(*authors_obj)
            return redirect('show')
        else:
            print(form_obj.errors)
            return render(request, 'book_add.html', {'form_obj': form_obj})

def show(request):
    # book_objs=Book.objects.all().select_related('publish').prefetch_related('authors')
    #5.94 ms (6 queries )
    book_objs=Book.objects.all().select_related('publish')  # 3.95 ms (4 queries )
    # book_objs=Book.objects.all().prefetch_related('authors')
    #10.04 ms (21 queries including 15 similar and 13 duplicates )
    # book_objs=Book.objects.all()#5.98 ms (19 queries including 15 similar and 13 duplicates )
    book_obj=book_objs.first()
    print(book_obj.publish)
    publish=Publish.objects.all()[1]
    print(publish.book_set.all())

    # egon=Author.objects.filter(name='司马迁').select_related('authorDetail')[0]
    egon=Author.objects.filter(name='司马迁')[0]
    print(egon.authorDetail.telephone)

    authorDet=AuthorDetail.objects.filter(addr='北京')[0]
    print(authorDet.author.name)
    # print(book_objs[0].atime)

    print(book_objs[7])
    authors=book_objs[7].authors.all()
    for a in authors:
        print(a.name,a.authorDetail.telephone)

    author=Author.objects.get(name='司马迁')
    book_list=author.book_set.all().values('title','publishDate','price')
    for b in book_list:
        # print(b.title)
        print(b)
    # print(book_list)
    return render(request,'book_list.html',{'book_objs':book_objs})

class CourseSerializers(serializers.Serializer):
# 这里面写对应的字段  写了那些字段  就会对那些字段的数据进行序列化  没有被序列化等字段 不会有返回数据
    title=serializers.CharField(max_length=32,required=False)
    price=serializers.CharField(max_length=8)
    publishDate = serializers.CharField(max_length=10)
    publish_id=serializers.IntegerField()

class CourseView(APIView,CacheResponseMixin):
    # 写一个类属性  名字必须是parser_classes
    parser_classes = [JSONParser,]
    @method_decorator(cache_page(60*2))
    @method_decorator(vary_on_cookie)
    def get(self,request):
        book_list=Book.objects.all()
        cs=CourseSerializers(book_list,many=True)
        se_data=cs.data
        print(se_data)
        ret=[]
        for book_obj in book_list:
            ret.append({
                'title':book_obj.title,
                'price':str(book_obj.price)
            })
        # return HttpResponse(json.dumps(ret,ensure_ascii=False))#第一种序列化  手动序列化

        # se_data=serialize('json',book_list,ensure_ascii=False)
        # print(se_data)
        return Response(se_data)
        # return Response(json.dumps(ret,ensure_ascii=False))
    # [{\"title\": \"西游记\", \"price\": \"100.00\"}
    @cache_response(timeout=60*3,cache='default')
    def post(self,request):
        print(request.POST)
        print(type(request))#<class 'rest_framework.request.Request'>
        print(request.data)     #{'name': 'chao'}
        # 发过来的数据  drf的序列化组件还能校验数据
        cs=CourseSerializers(data=request.data,many=False)
        print(cs.is_valid())  # 如果少数据  一条数据不完整  得到的是False
        if cs.is_valid():
            print(cs.data)
            Book.objects.create(**cs.data)
            return Response(cs.data)
        else:
            cs_errors=cs.errors
            return Response(cs_errors)

        # return HttpResponse('POST')


def noramal(request):
    print(request.body)
    # django没有内置的自动解开json数据类型的方法  只能去request.body里面那原始的bytes类型的数据  然后自己解
    print(json.loads(request.body.decode("utf8")))
    # Django自动通过contentType解析数据的方法就叫做Django的解析器 能解的urlencode和文件的那个mutipart/form-data
    print(type(request))
    return HttpResponse('POST')


# Create your views here.
def login(request):
    pass

def index(request):
    # print(reverse('index'))

    print(reverse('app02:index'))
    return HttpResponse('app02')