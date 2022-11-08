from rest_framework.permissions import BasePermission


#权限组件
class SVIPPermission(BasePermission):
    message="SVIP才能访问！"   #变量只能叫做message
    def has_permission(self, request, view):
        print(request.user)
        if request.user.user_type==3:
            return True
        return False