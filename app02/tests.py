from django.test import TestCase

# Create your tests here.
from  app02.models import  *

publish_obj=Publish.objects.get(nid=2)

print(publish_obj)
# book_obj=Book.objects.create(title='西游记',publishDate='2012-12-12',price=100,publish=publish_obj)

book_obj=Book.objects.create(title='追风筝的人',publishDate='2012-11-12',price=200,publish_id=1)
yuan=Author.objects.filter(name='yuan').first()
egon=Author.objects.filter(name='alex').first()
print(yuan.name)
print(egon)
book_obj.authors.add(yuan,egon)