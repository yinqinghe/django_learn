
# 一个库中写入  多个库中读取
class Router:
    def db_for_read(self,model,**kwargs):
        # 分库   app01使用default数据库    app02使用db2
        # if model._meta.app_label=='app01':
        #
        #     return 'default'
        # if model._meta.app_label=='app02':
        #     return "db2"
        return 'default'

    def db_for_write(self,model,**kwargs):
        print('db2')
        return 'db2'