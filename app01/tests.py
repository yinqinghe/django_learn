from django.test import TestCase

# Create your tests here.

# from django.db import models
from  app01.models import  *
e = LmsUser.objects.filter(mobile=185363843).first()
a=Author.objects.get(id=1)
print(e.email)
print(a.name)