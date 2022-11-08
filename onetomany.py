import os


if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","bms.settings")
    import  django

    django.setup()

    from onetomany.models import *
    #
    # Project.objects.create(name="电商项目",describe="电商项目描述...")
    # Project.objects.create(name="在线教育项目",describe="在线教育项目描述。。")
    # Project.objects.create(name="大数据项目",describe="大数据项目描述。。。")

    #
    # project_obj=Project.objects.get(name='电商项目')
    # App.objects.create(name='product',describe='商品服务',project=project_obj)
    # App.objects.create(name='order',describe='订单服务',project=project_obj)

# 正向查询
    app=App.objects.get(name='product')
    print(app.project.name)

    app_list=App.objects.all().only('name')
    print(app_list)
    for i in app_list:
        print(i.name,i.project.name,i.project.describe)

# 反向查询
    project=Project.objects.get(name="电商项目")
    project.app_set.all()  #根据获取的项目  查询所有应用

    project=Project.objects.all()
    for i in project:
        print(i.name,i.app_set.all())