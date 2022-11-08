from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from app05.models import *
from app05.serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from utils.permissions import *
from rest_framework.decorators import api_view,permission_classes
from django.conf import settings


# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated))
def example_view(request,format=None):
    content={'status':'request was permitted'}
    return HttpResponse(content)

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #important
    def perform_create(self, serializer):
        serializer.save(author=settings.AUTH_USER_MODEL)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class Articles(APIView):
    def get(self, request):
        article_list = Article.objects.all()
        cs = ArticleSerializer(article_list, many=True)
        se_data = cs.data
        print(se_data)

        return Response(se_data)
    def post(self,request):
        cs=ArticleSerializer(data=request.data,many=False)
        print(cs.is_valid())  # 如果少数据  一条数据不完整  得到的是False
        if cs.is_valid():
            print(cs.data)
            Article.objects.create(**cs.data)
            return Response(cs.data)
        else:
            cs_errors=cs.errors
            return Response(cs_errors)
