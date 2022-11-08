from django.contrib import admin

# Register your models here.
from app01.models import *

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(LmsUser)
admin.site.register(cctime)

admin.site.register(add_time1)
