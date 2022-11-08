from app03.models import *
from rest_framework import serializers
import django_filters
class PublishSerializers_f(django_filters.FilterSet):
    city_qq=django_filters.CharFilter(field_name='city',lookup_expr='icontains')#内容中包含
    # nid_gt=django_filters.CharFilter(field_name='nid',lookup_expr='gt')#大于该值
    # nid_lt=django_filters.CharFilter(field_name='nid',lookup_expr='lt')#小于该值
    name=django_filters.CharFilter(field_name='name',lookup_expr='icontains')#内容中包含

    class Meta:
        model=Publish
        fields = ('email', 'city')
        # fields="__all__"
        # fields={'nid':['lt','gt'], }#查询字段nid__lt
class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model=Author
        fields = ('name', 'age')
class BookSerializers_(serializers.HyperlinkedModelSerializer):
    # publish=serializers.HyperlinkedIdentityField(
    #     view_name='publish_book',
    #     # lookup_field='publish_id',
    #     # lookup_url_kwarg='pk',
    # )
    class Meta:
        model=Book
        fields=['title','price']

class PublishSerializers(serializers.ModelSerializer):
    class Meta:
        model=Publish
        fields="__all__"

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"



