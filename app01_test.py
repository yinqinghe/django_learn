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

    article_list=Author.objects.all()

    archive_dict={}
    for article in article_list:
        name=article.name
        archive_dict.setdefault(name,{'name':name,'article_list':[]})
        archive_dict[name]['article_list'].append(article)

        context={
            'archive_list':archive_dict.values(),
            'article_count':len(article_list),
        }
        serializer_archives=[]
        for archive in archive_dict.values():
            serializer_archives.append({
                'name':archive['name'],
                # 'article_list':serializers.serialize('json',archive['article_list'])
            })
        cache.set('rediskey',json.dumps(serializer_archives))
        cache.expire('rediskey',30)


    #     redis_value=cache.get('rediskey')
    #     if redis_value:
    #         print('hit cache')
    #         serializer_archives=json.loads(redis_value)
    #
    # # conn=redis.Redis(connection_pool=pool)   #redis连接池
    # # print(conn.set('test_key','test_value'))
    conn=get_redis_connection('sms_code')    #使用django-redis
    print(conn.set('test_key','test_value'))
    conn.expire('test_key',60*60)
    print(conn.get('test_key'))

    # cache.set('foo','value',timeout=None)
    # cache.set('foo1','value',timeout=None)
    # cache.set('foo2','value',timeout=None)
    #
    # print(    cache.ttl('foo'))
    # print(cache.ttl('not-existent'))
    # # 通配符搜索的烈子
    # print(cache.keys('foo*'))
    # # 如果数据量比较大这样就不太合适   可以使用迭代器
    # print(cache.iter_keys('foo*'))
    # print(next(cache.iter_keys('foo*')))