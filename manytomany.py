import os

if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","bms.settings")
    import  django

    django.setup()

    from onetomany.models import *

    # Server.objects.create(hostname="ec-test1",ip='192.168.1.10',describe="电商项目测试服务器1")
    # Server.objects.create(hostname="ec-test1",ip='192.168.1.11',describe="电商项目测试服务器2")
    # Server.objects.create(hostname="bigdata-test1",ip='192.168.1.11',describe="大数据项目测试服务器1")

    # project_obj=Project.objects.get(name="电商项目")
    # app=App.objects.create(name="portal",describe="前端服务",project=project_obj)
    # server=Server.objects.get(hostname="ec-test1")
    # server.app.add(app)

    app=App.objects.get(name='order')
    server=Server.objects.get(hostname='ec-test1')
    # server.app.add(app)    添加
    # server.app.remove(app)   移除

    server.app.clear()   #将该服务器取消所有应用关联
# 正向查询
    server=Server.objects.get(hostname='ec-test1')
    ser=server.app.all()
    # print(ser)
    server_list=Server.objects.all()
    for i in server_list:
        print(i.hostname,i.app.all())

    print('++++++++++++++++++++++++++')
# 反向查询
    app=App.objects.get(name='portal')
    app.server_set.all()

    app_list=App.objects.all()
    for i in app_list:
        print(i.name,i.server_set.all())