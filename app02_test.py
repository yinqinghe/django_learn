import os
import json
from datetime import datetime
from datetime import date

import pytz
from django.db.models import Count,Avg,Max,Min,Sum
if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","bms.settings")
    import  django

    django.setup()

    from app02.models import *
#正向查询  一对多
    # queryResult=Book.objects.filter(publish__name="苹果出版社").values_list('title')
# 反向查询  一对多
#     queryResult=Publish.objects().filter(name='苹果出版社').values_list('book__title','book__price')

# 正向查询   多对多
    queryResult=Book.objects.filter(authors__name="司马迁").values_list('title')
# 反向查询   多对多
#     queryResult=Author.objects.filter(name='司马迁').values_list('book__title','book__price')

 # 正向查询  一对一
 #    queryResult=Author.objects.filter(name='张居正').values('authorDetail__telephone')
 # 反向查询    一对一
 #    queryResult=AuthorDetail.objects.filter(author__name='张居正').values('telephone')


#   正向查询   连续跨表查询
#     queryResult=Book.objects.filter(publish__name='苹果出版社').values('title','authors__name')
#   反向查询   连续跨表查询
#     queryResult=Publish.objects.filter(name="苹果出版社").values('book__title','book__authors__age','book__authors__name')

# 练习：查出手机号以1开头的作者出版过得所有书籍名称及出版社名称
#     方式一
#     queryResult=Book.objects.filter(authors__authorDetail__telephone__regex='1').values('title','publish__name','authors__authorDetail__telephone')
    # 方式二
    # queryResult=Author.objects.filter(authorDetail__telephone__startswith='91').values('book__title','book__publish__name','authorDetail__telephone')



# 聚合查询
    queryResult=Book.objects.all().aggregate(avg=Avg('price'),max=Max('price'),)
# 分组查询
    queryResult=


    print(queryResult)
    # for q in queryResult:
    #     print(q)
















    publish_obj=Publish.objects.get(nid=2)

    print(publish_obj)
    # book_obj=Book.objects.create(title='西游记',publishDate='2012-12-12',price=100,publish=publish_obj)

    # book_obj=Book.objects.create(title='追风筝的人',publishDate='2012-11-12',price=200,publish_id=2)
    # yuan=Author.objects.filter(name='yuan').first()
    # egon=Author.objects.filter(name='alex').first()
    # print(yuan.name)
    # print(egon)
    # book_obj.authors.add(yuan,egon)

    book=Book.objects.all()
    # for i in book:
    #     print(i.title,i.authors.all())

    # book=Book.objects.filter(nid=10)[0]
    # book.authors.remove(2)
    # book.authors.set('2')
    # Book.objects.filter(title='追风筝的人').delete()

    # 基于双下划线的模糊查询
    # books=Book.objects.filter(price__in=[100,200,300])#price值等于这三个里面的任意一个的对象
    # books=Book.objects.filter(price__gt=100)#price大于100   大于等于gte
    # books=Book.objects.filter(price__lt=100)#price小于100   小于等于lte
    # books=Book.objects.filter(price__range=[100,200])#sql的between  and  大于等于100  小于等于200
    # books=Book.objects.filter(title__contains="python")#内容里包含  切准确区分大小写
    # books=Book.objects.filter(title__icontains="python")#不区分大小写
    # books=Book.objects.filter(title__istartswith='py')#以什么开头  istartswith  不区分大小写
    # books=Book.objects.filter(publishDate__year=2012)#

    # books=Book.objects.filter(publishDate__year__gt=2012)#找大于2012年的所有书籍
    # books=Book.objects.filter(publishDate__year=2012,publishDate__month=12)#找出2012年2月的书籍

    # books=Book.objects.all().distinct()#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.all().distinct("price")#报错  不能再ditinct里面加字段名称
    # books=Book.objects.values('price').distinct()#报错  不能再ditinct里面加字段名称
    # books=Book.objects.all().values('price').distinct()#{'price': Decimal('100.00')}
    # books=Book.objects.all().values_list('price','title').distinct()#(Decimal('100.00'),)

    # books=Book.objects.all().values('nid','title')#这里什么不写就是去重  所有的字段重复才叫重复

    # books=Book.objects.exclude(title__contains="山").order_by('-price')#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.exclude(title__contains="山").count()#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.exclude(title__contains="山").reverse()#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.exclude(title__contains="山")#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.exclude(title__contains="山").first()#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.exclude(title__contains="山").last()#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.exclude(title__contains="山").exists()#这里什么不写就是去重  所有的字段重复才叫重复
    # books=Book.objects.exclude(title__contains="山").values('nid','title','price')#{'nid': 1, 'title': '西游记', 'price': Decimal('100.00')}   value返回的是一个字典序列
    # books=Book.objects.exclude(title__contains="山").values_list('nid','title','price')#(1, '西游记', Decimal('100.00'))  values_list返回一个元祖序列

    # books=Book.objects.values('price','title').annotate(nid_count=Count('pk',distinct=True))#(1, '西游记', Decimal('100.00'))  values_list返回一个元祖序列
    # books=Book.objects.dates('publishDate','year','DESC')#(1, '西游记', Decimal('100.00'))  values_list返回一个元祖序列
    # books=Book.objects.datetimes('atime','year','DESC',tzinfo=pytz.timezone('Asia/Shanghai'))#(1, '西游记', Decimal('100.00'))  values_list返回一个元祖序列
    # books=Book.objects.aggregate(k=Count('price',distinct=True),n=Count('title',distinct=True))#(1, '西游记', Decimal('100.00'))  values_list返回一个元祖序列

    # obj,books=Book.objects.get_or_create(title='世界经济史',price='50.0',publishDate='2000-1-18',publish_id=1)#(1, '西游记', Decimal('100.00'))  values_list返回一个元祖序列
    # books=Book.objects.in_bulk([11,12,13,15,16,17])#(1, '西游记', Decimal('100.00'))  values_list返回一个元祖序列
    books=Book.objects.raw('select * from app02_book',using='default')#执行原生SQL


    # for i in books:
    #     print(i.title,i.price,i.authors.all())
        # print(i)
    # print(books.fetchone(),'------')

    from django.db import connection,connections
    cursor=connection.cursor()
    cursor.execute("select * from app02_book")
    # print(cursor.fetchone())
    # print(cursor.fetchall())
    # print(cursor.fetchmany())
    #
    #
    # book_obj=Book.objects.filter(pk=1).first()
    # print(book_obj.publish)

    # 对含有日期格式数据的json数据进行转换
    # class JsonCustomEncoder(json.JSONEncoder):
    #     def default(self, field) :
    #         if isinstance(field,datetime):
    #             return field.strftime('%Y-%m-%d %H:%M:%S')
    #         elif isinstance(field,date):
    #             return field.strftime('%Y-%m-%d')
    #         else:
    #             return json.JSONEncoder.default(self,field)
    #
    # d1=datetime.now()
    # print(d1)
    # dd=json.dumps(d1,cls=JsonCustomEncoder)
    # print(dd)