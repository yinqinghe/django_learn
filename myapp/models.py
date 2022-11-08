from django.db import models

# Create your models here.


class IdCard(models.Model):
    number=models.CharField(max_length=18,verbose_name="身份证号")
    address=models.CharField(max_length=100,verbose_name="地址")
    user=models.OneToOneField(to='User',to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table="idcard"
        verbose_name_plural="身份证表"

    def __str__(self):
        return  self.number


class User(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=18,verbose_name="身份证号")
    name=models.CharField(max_length=32,verbose_name="名称")
    sex=models.CharField(max_length=4,verbose_name="性别")
    age=models.IntegerField(verbose_name="年龄")
    label=models.CharField(max_length=100,verbose_name="标签")

