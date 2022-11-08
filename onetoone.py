import os


if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","bms.settings")
    import  django

    django.setup()

    from myapp.models import *


    # user_obj=User.objects.create(user='mike',name='迈开',sex='女',age='25',label='篮球，神，黑猫')
    # IdCard.objects.create(user=user_obj,number='98877',address='芝加哥')
    # print(user_obj)

    # user_obj=User.objects.get(user="zhangsan")
    # IdCard.objects.create(user=user_obj,number='123456',address='湖南')
# 查
# 反向查询
    user=User.objects.get(user='zhangsan')
    print(user.idcard.number)
    print(user.idcard.address)

# 正向查询
    idcard=IdCard.objects.get(user_id=1)
    print(idcard.user.user)
    print(idcard.user.name)

# 改
    user_obj=User.objects.get(user='zhangsan')
    user_obj.idcard.address='河南'
    user_obj.idcard.save()

# 删
    User.objects.filter(user='alan').delete()
