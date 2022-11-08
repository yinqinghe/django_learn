from django.db import models

# Create your models here.

class User(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    type_choice=((1,"VIP"),(2,"SVIP"),(3,"SSVIP"))
    user_type=models.IntegerField(choices=type_choice)

class UserToken(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    token=models.CharField(max_length=128)
    expire_time=models.DateTimeField()