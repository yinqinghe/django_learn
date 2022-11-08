import json
import os

from django.core.cache import cache
from django_redis import get_redis_connection, serializers
from utils.redis_pool import pool
import redis
if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","bms.settings")
    import  django

    django.setup()

    from app01.models import *

    article_list=Author.objects.using('db2').all()
    for i in article_list:
        print(i.name)
    Author.objects.create(name='老舍',sex='男',age='76',tel='10086')