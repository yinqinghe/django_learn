from django.db import models
from django.conf import settings
# Create your models here.


class Article(models.Model):
    STATUS_CHOICES=(
        ('p','Published'),('d','Draft'),
    )
    title=models.CharField(verbose_name='Title',max_length=90,db_index=True)
    body=models.TextField(verbose_name='Body',blank=True)
    author=models.ForeignKey(to=settings.AUTH_USER_MODEL,to_field='id',verbose_name='Author',on_delete=models.CASCADE)
    status=models.CharField(verbose_name='Status',max_length=1,choices=STATUS_CHOICES,default='s',null=True,blank=True)
    create_date=models.DateTimeField(verbose_name='CDatetime',auto_now_add=True)

    def __str__(self):
        return self.title