from app04.models import *
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
