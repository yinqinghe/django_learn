import datetime
import hashlib

from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect
from app01.models import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.cache import cache_page
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def more_database(request):
    article_list=Author.objects.using('db2').all()
    for i in article_list:
        print(i.name)
    aa=Author.objects.create(name='老舍11',sex='男',age='76',tel='10086')
    return HttpResponse(aa)

# @cache_page(30*15)
# @login_required
def index(request):
    print('user:', request.user)
    print('user_id:', request.user.id)
    print('user_username:', request.user.username)
    print('user_is_active:', request.user.is_active)
    request.session['k12']=1230101
    print(request.session.items())
    print(request.session.session_key)
    # request.session.flush()
    # print(reverse('app01:index'))
    return HttpResponse('app01index')

def time_op(request):
    print(request.GET)
    print(request.GET.get('date'))#2022-11-11
    print(request.GET.get('color'))  ##000000
    print(request.GET.get('time'))  #15:04
    print(request.GET.get('datetime-local')) #2022-11-11T15:01
    print(request.GET.get('month'))   #2022-06
    print(request.GET.get('week'))   #2022-W44
    date=str(request.GET.get('date'))
    time1=str(request.GET.get('time'))

    datetime_=request.GET.get('datetime-local')
    month=request.GET.get('month')
    week=request.GET.get('week')

    # obj=add_time1.objects.create(bools=True,datetime='{0} {1}'.format(date,time1),date=date)
    add_time1.objects.filter(id=1).update(bools=False,change_date=datetime.datetime.now())

    # _t=add_time1.objects.get(id=1)
    # _t.bools=False
    # _t.save()
    new_name='新华社出版'
    new_addr='北京'
    # obj=Publisher.objects.create(name=new_name, addr=new_addr)

    # print(obj)
    return HttpResponse('sucess!!')

def publisher_list(request):
    publisher=Publisher.objects.all()
    return  render(request,'pub_list.html',{'pub_list':publisher})


def add_publisher(request):
    if request.method=='POST':
        new_pubslisher_name=request.POST.get('name')
        new_pubslisher_addr=request.POST.get('addr')
        Publisher.objects.create(name=new_pubslisher_name,addr=new_pubslisher_addr)
        return  redirect('/pub_list/')
    return  render(request,'pub_add.html')


def edit_publisher(request):
    if request.method=='POST':
        edit_id=request.GET.get('id')
        edit_obj=Publisher.objects.get(id=edit_id)
        new_name=request.POST.get('edit_name')
        new_addr=request.POST.get('edit_addr')
        edit_obj.name=new_name
        edit_obj.addr=new_addr
        edit_obj.save()
        return redirect('/pub_list/')
    edit_id=request.GET.get('id')
    edit_obj=Publisher.objects.get(id=edit_id)
    return  render(request,'pub_edit.html',{'publisher':edit_obj})

def drop_publisher(request):
    drop_id=request.GET.get('id')
    drop_obj=Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/pub_list')

# @ensure_csrf_cookie
def author_list(request):
    author=Author.objects.all()
    # print(author)
    return  render(request,'auth_list.html',{'author_list':author})

def add_author(request):
    print('--------------',request.method)

    if request.method=='POST':
        new_author_name=request.POST.get('name')
        new_author_sex=request.POST.get('sex')
        new_author_age=request.POST.get('age')
        new_author_tel=request.POST.get('tel')
        print(new_author_name)
        Author.objects.create(name=new_author_name,sex=new_author_sex,age=new_author_age,tel=new_author_tel)
        return  redirect('/author_list/')
    return  render(request,'author_add.html')

def drop_author(request):
    drop_id=request.POST.get('id')
    print(request.POST)
    print(request.POST.get('fname'))

    print(drop_id)
    drop_obj=Author.objects.get(id=drop_id)
    # drop_obj.delete()
    return  redirect('/author_list/')

def edit_author(request):
    if request.method=='POST':
        edit_id=request.POST.get('id')
        print(edit_id)
        edit_obj=Author.objects.get(id=edit_id)
        new_author_name=request.POST.get('edit_name')
        new_author_sex=request.POST.get('edit_sex')
        new_author_age=request.POST.get('edit_age')
        new_author_tel=request.POST.get('edit_tel')
        new_book_id=request.POST.getlist('book_id')
        print(new_book_id)
        edit_obj.name=new_author_name
        edit_obj.sex=new_author_sex
        edit_obj.age=new_author_age
        edit_obj.tel=new_author_tel
        edit_obj.book.set(new_book_id)
        edit_obj.save()
        return  redirect('/author_list')
    edit_id=request.GET.get('id')
    edit_obj=Author.objects.get(id=edit_id)
    all_book=Book.objects.all()
    return  render(request,'auth_edit.html',{
        'author':edit_obj,
        'book_list':all_book
    })


def book_list(request):
    print(request.session.items())
    if request.session.exists(request.session.session_key):   #验证用户是否登录
        book=Book.objects.all()
        return  render(request,'book_list.html',{'book_list':book})
    else:
        return redirect('login')

def add_book(request):
    if request.method=='POST':
        new_book_name=request.POST.get('name')
        new_book_ISBN=request.POST.get('ISBN')
        new_book_translator=request.POST.get('translator')
        new_book_date=request.POST.get('date')
        publisher_id=request.POST.get('publisher_id')
        Book.objects.create(name=new_book_name,publisher_id=publisher_id,ISBN=new_book_ISBN,translator=new_book_translator,date=new_book_date)

        return  redirect('/book_list/')
    res=Publisher.objects.all()
    return  render(request,'book_add.html',{'publisher_list':res})

def drop_book(request):
    drop_id=request.GET.get('id')
    drop_obj=Book.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/book_list/')

def edit_book(request):
    if request.method=='POST':
        new_book_name = request.POST.get('name')
        new_book_ISBN = request.POST.get('ISBN')
        new_book_translator = request.POST.get('translator')
        new_book_date = request.POST.get('date')
        new_publisher_id = request.POST.get('publisher_id')
        edit_id=request.GET.get('id')
        edit_obj=Book.objects.get(id=edit_id)
        edit_obj.name=new_book_name
        edit_obj.ISBN=new_book_ISBN
        edit_obj.translator=new_book_translator
        edit_obj.date=new_book_date
        edit_obj.publisher_id=new_publisher_id
        edit_obj.save()
        return redirect('/book_list/')
    edit_id=request.GET.get('id')
    edit_obj=Book.objects.get(id=edit_id)
    all_publisher=Publisher.objects.all()
    return  render(request,'book_edit.html',{'book':edit_obj,'publisher_list':all_publisher})

def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    password=md5.hexdigest()
    return  str(password)

def logins(request):
    if request.method=='POST' and request.POST:
        print('----------', request.method)

        email=request.POST.get('email')
        print(email)
        password=request.POST.get('password')
        # e=LmsUser.objects.filter(email=email).first()
        # print(e)
        user_obj=authenticate(username=email,password=password)
        print(user_obj)
        if user_obj:
            login(request,user_obj)
            now_password=setPassword(password)
            # db_password=e.password
            # if now_password==db_password:
            request.session['login']='successs'
            reponse=HttpResponseRedirect('/pub_list')
            reponse.set_cookie('username',email)
            return  reponse
    return  render(request,'login.html')

def register(request):
    print('++++++++++++',request.method)
    if request.method=='POST' and request.POST:
        data=request.POST
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        mobile=data.get('mobile')
        # exits=LmsUser.objects.get(username=username)
        # print(exits)
        user_obj=authenticate(email=email,password=password)
        print(user_obj)
        if user_obj:
            print('该用户已存在')
            return HttpResponse('该用户已存在')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)

            LmsUser.objects.create(
                username=username,
                email=email,
                password=setPassword(password),
                mobile=mobile,
            )
            return  HttpResponseRedirect('/login/')
    return render(request,'register.html')

def logoutd(request):
    logout(request)
    return redirect(reverse('login'))

@login_required
def set_password(request):
    print(request.POST)
    request.user.set_password()
    request.user.save()

    return redirect(reverse('login'))