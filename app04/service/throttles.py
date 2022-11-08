from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
import time
from rest_framework import exceptions
visit_record={}

# 频率组件
# class VisitThrottle1(SimpleRateThrottle):
#     scope = 'visit_rate'
#     def get_cache_key(self, request, view):
#         return self.get_ident(request)

class VisitThrottle(BaseThrottle):
    # 限制访问时间
    VISIT_TIME=10
    VISIT_COUNT=3

    # 定义方法  方法名和参数不能变
    def allow_request(self, request, view):
        # 获取登录主机的id
        id=request.META.get('REMOTE_ADDR')
        print('id',id)
        self.now=time.time()

        if id not in visit_record:
            visit_record[id]=[]

        self.history=visit_record[id]
        print(self.history)
        # 限制访问时间
        while self.history and self.now-self.history[-1]>self.VISIT_TIME:
            self.history.pop()
        # 此时history中只保存了最近10秒钟的访问记录
        if len(self.history)>=self.VISIT_COUNT:
            return False
        else:
            self.history.insert(0,self.now)
            return True

    def wait(self):
        return self.history[-1]+self.VISIT_TIME-self.now