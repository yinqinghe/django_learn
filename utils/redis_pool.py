import redis

pool=redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=1000,password=123456)