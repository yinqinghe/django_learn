from app05.models import *
from rest_framework import serializers
from django.conf import settings
# 验证器
def multiple_of_ten(value):
    if value%10!=0:
        raise serializers.ValidationError("NOt a multiple of ten")
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=settings.AUTH_USER_MODEL
        fields=('id','username','email')
    def create(self, validated_data):
        print('User',validated_data)

#对象级别验证
class EventSerializer(serializers.Serializer):
    # score=serializers.IntegerField(validators=[multiple_of_ten()])

    description=serializers.CharField(max_length=100)
    start=serializers.DateTimeField()
    finish=serializers.DateTimeField()

    def validators(self,data):
        if data['start']>data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
class ArticleSerializer(serializers.ModelSerializer):
    # author=UserSerializer(required=False,read_only=True)#  使用嵌套序列化器
    # author=serializers.ReadOnlyField(source="settings.AUTH_USER_MODEL.username")
    status=serializers.ReadOnlyField(source="get_status_display")
    full_status=serializers.ReadOnlyField(source="get_status_display")
    cn_status=serializers.SerializerMethodField()
    title=serializers.CharField(max_length=100)
    # author_id=serializers.CharField(max_length=32,source='article.user')
    def validated_title(self,value):   #字段级别验证
        if 'django' not in value.lower():
            raise serializers.ValidationError("Article is not about Django")
        return value
    class Meta:
        model=Article
        fields='__all__'

        # read_only_fields=('id','author','create_date')
        # depth=1  #通过设置关联模型的深度   优点  简单  缺点  表的字段全部暴露出来

    # def create(self, validated_data):
    #     print(validated_data)
    #     author_data=validated_data.pop('author')
    #     print(author_data)
    #     print(validated_data)
    #     # user=settings.AUTH_USER_MODEL.objects.create(**validated_data)
    #     art=Article.objects.create(**validated_data)
    #     return art

    def get_cn_status(self,obj):
        if obj.status=='p':
            return "已发表"
        elif obj.status=='d':
            return "草稿"
        else:
            return 'blank'
    def get_full_status(self,obj):
        if obj.status=='p':
            return "已发表full"
        elif obj.status=='d':
            return "草稿full"
        else:
            return 'blank'
