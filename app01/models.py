from django.db import models

# Create your models here.

# 出版社类
class Publisher(models.Model):
    id=models.AutoField('序号',primary_key=True)
    name=models.CharField('名称',max_length=64)
    addr=models.CharField('地址',max_length=64)

    class Meta:
        # verbose_name_plural='出版社'
        # 不加plural  admin显示汉字后面加s
        verbose_name='出版社'
    # def __str__(self):
    #     return self.id
# 书籍类
class Book(models.Model):
    id=models.AutoField('序号',primary_key=True)
    name=models.CharField('名称',max_length=64,null=True)
    ISBN=models.CharField('编号',max_length=64)
    translator=models.CharField('译者',max_length=64)
    date=models.DateField('出版日期',max_length=64,blank=True)
    publisher=models.ForeignKey(to=Publisher,on_delete=models.CASCADE)
    # class Meta:
    #     verbose_name_plural='书籍'
# 作者的类
class Author(models.Model):
    id = models.AutoField('序号', primary_key=True)  #help_text提示信息
    name = models.CharField('名称aa', max_length=64,help_text='不要写外国名')
    sex=models.CharField(verbose_name='性别',max_length=4)
    # choices = ((0, 'male'), (1, 'female')),
    age=models.IntegerField(verbose_name='年龄')#edotable  false  不显示在admin
# Django中创建外键联表操作
    tel=models.CharField(verbose_name='联系方式',max_length=64)
# 一个作者可以对应多本书  一本书也可以有多个作者  多对多   在数据库中创建第三张表
    book=models.ManyToManyField(blank=True,to=Book)

    class Meta:
        verbose_name_plural='作者'
    # 这个函数是让admin列出每条数据时  显示出返回的字段内容  便于前段展示
    # def __str__(self):
    #     return [self.name,self.sex]
# 用户的类
class LmsUser(models.Model):
    id=models.AutoField('序号',primary_key=True)
    username=models.CharField('用户名',max_length=32)
    password=models.CharField('密码',max_length=32)
    email=models.EmailField('邮箱')
    mobile=models.CharField('手机',max_length=11)

class cctime(models.Model):
    # 时间格式 YYYY-MM-DD 相当于MYSQL  date类型
    date=models.DateField(blank=True,auto_now=True)  #自动更新时间 添加或修改  都是当前操作的时间
    dates=models.DateField(blank=True,auto_now_add=True)  #永远是创建时的时间
    # 时间格式   YYYY-MM-DD HH:MM:SS      相当于MYSQL  datetime  timestamp类型
    now_datetime=models.DateTimeField(auto_now=True)
    # now_add_datetime=models.DateTimeField(auto_now_add=True)
    datetime=models.DateTimeField(blank=True)
    filepath=models.FilePathField(blank=True,path=r'D:\C#\python\Django\django_2022\bms\media')
    ipadd=models.GenericIPAddressField(default=0)
    booleans=models.BooleanField(default=False)
    file=models.FileField(upload_to='media')
    # 时间格式    HH:MM:SS
    ctime=models.TimeField(default=0)

    class Meta:
        verbose_name_plural='时间'

class add_time1(models.Model):
    bools=models.BooleanField(default=False)
    change_date = models.DateTimeField(blank=True, auto_now=True)  # 自动更新时间 添加或修改  都是当前操作的时间
    add_date = models.DateTimeField(blank=True, auto_now_add=True)  # 永远是创建时的时间
    datetime=models.DateTimeField(blank=True)
    # ctime=models.TimeField(default=100)
    date=models.DateField(blank=True)  #自动更新时间 添加或修改  都是当前操作的时间

