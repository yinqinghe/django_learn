from django.db import models

# Create your models here.


class Author(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='作者姓名')
    age=models.IntegerField()


    authorDetail=models.OneToOneField(to='AuthorDetail',to_field='nid',on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name},{self.nid}'
    # books=models.ManyToManyField(to='Book',related_name='authors')
class AuthorDetail(models.Model):
    nid=models.AutoField(primary_key=True)
    brithday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField(max_length=64)

class Publish(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)
    email=models.EmailField()
    def __str__(self):
        return f'{self.name,self.nid}'

class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    publish=models.ForeignKey(to='Publish',to_field='nid',on_delete=models.CASCADE)
    ctime=models.DateTimeField(auto_created=True,null=True)
    atime=models.DateTimeField(auto_now_add=True,null=True)
    authors=models.ManyToManyField(to='Author')