from app03.models import *
from app04.models import *
from rest_framework.exceptions import AuthenticationFailed
#认证组件
class Authentication():
    # 每个认证类 都需要有个authenticate_header方法  并且有个参数request
    def authenticate_header(self,request):
        pass
    # authenticate方法固定的  并且必须有个参数  这个参数的新的request对象
    def authenticate(self,request):
        # if request.method=="OPTIONS":
        #     return
        # token=request._request.GET.get("token")#这是老的request对象封装到了新的request对象中
        token=request.query_params.get('token')
        # 用户请求来了之后  我们获取token值  到数据库中验证
        usertoken=UserToken.objects.filter(token=token).first()
        print('usertoken',usertoken)
        print('usertoken.user',usertoken.user)
        if usertoken:
            # 验证成功后  可以返回两个值  也可以什么都不返回
            # return {"user":usertoken.user.user,"user_type":usertoken.user.user_type},usertoken.token
            return usertoken.user, usertoken.token

        else:
            # 因为源码内部进行了异常捕获  并且给你主动返回一个forbiden错误   这里主动抛出异常
            return AuthenticationFailed("认证失败")

        # if 1:
        ##这个方法返回两个值  并且这两个返回值封装到了新的request对象中了 request.user-->用户名
        # 和request.auth-->token值  这两个值作为认证结束后的返回结果
        #     return "user:jordan","auth:abcabc"