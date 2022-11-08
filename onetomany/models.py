from django.db import models

# Create your models here.

class Project(models.Model):
    name=models.CharField(max_length=30)
    describe=models.CharField(max_length=100)
    datatime=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="project"
        verbose_name_plural="项目表"

    def __str__(self):
        return self.name

class App(models.Model):
    name=models.CharField(max_length=30)
    describe=models.CharField(max_length=100)
    datatime=models.DateTimeField(auto_now_add=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)

    class Meta:
        db_table="app"
        verbose_name="应用表"

    def __str__(self):
        return  self.name

class Server(models.Model):
    hostname=models.CharField(max_length=30)
    ip=models.GenericIPAddressField()
    describe=models.CharField(max_length=100)
    datatime=models.DateTimeField(auto_now_add=True)

    app=models.ManyToManyField(App)
    class Meta:
        db_table="server"
        verbose_name_plural="服务器"

    def __str__(self):
        return  self.hostname
