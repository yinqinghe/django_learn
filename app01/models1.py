# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class App(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    describe = models.CharField(max_length=100)
    datatime = models.DateTimeField()
    project = models.ForeignKey('Project', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app'


class App01Author(models.Model):
    name = models.CharField(max_length=64)
    sex = models.CharField(max_length=4)
    age = models.IntegerField()
    tel = models.CharField(max_length=64)
    cdate = models.DateField(blank=True, null=True)
    cdatetime = models.DateTimeField(blank=True, null=True)
    ctime = models.TimeField(blank=True, null=True)
    ctimestamp = models.DateTimeField(blank=True, null=True)
    cyear = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'app01_author'


class App01AuthorBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(App01Author, models.DO_NOTHING)
    book = models.ForeignKey('App01Book', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app01_author_book'
        unique_together = (('author', 'book'),)


class App01Book(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=64)  # Field name made lowercase.
    translator = models.CharField(max_length=64)
    date = models.DateField()
    publisher = models.ForeignKey('App01Publisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app01_book'


class App01Lmsuser(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=254)
    mobile = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app01_lmsuser'


class App01Publisher(models.Model):
    name = models.CharField(max_length=64)
    addr = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'app01_publisher'


class App02Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    authordetail = models.OneToOneField('App02Authordetail', models.DO_NOTHING, db_column='authorDetail_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app02_author'


class App02Authordetail(models.Model):
    nid = models.AutoField(primary_key=True)
    brithday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'app02_authordetail'


class App02Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishdate = models.DateField(db_column='publishDate')  # Field name made lowercase.
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey('App02Publish', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app02_book'


class App02BookAuthors(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.ForeignKey(App02Book, models.DO_NOTHING)
    author = models.ForeignKey(App02Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app02_book_authors'
        unique_together = (('book', 'author'),)


class App02Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'app02_publish'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Idcard(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=18)
    address = models.CharField(max_length=100)
    user = models.OneToOneField('MyappUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'idcard'


class MyappUser(models.Model):
    user = models.CharField(max_length=18)
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=4)
    age = models.IntegerField()
    label = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'myapp_user'


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    describe = models.CharField(max_length=100)
    datatime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project'


class Server(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostname = models.CharField(max_length=30)
    ip = models.CharField(max_length=39)
    describe = models.CharField(max_length=100)
    datatime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'server'


class ServerApp(models.Model):
    id = models.BigAutoField(primary_key=True)
    server = models.ForeignKey(Server, models.DO_NOTHING)
    app = models.ForeignKey(App, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'server_app'
        unique_together = (('server', 'app'),)


class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
