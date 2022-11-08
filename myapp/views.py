from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def urls(request,id=1):
    print(id)
    return HttpResponse('ok')
