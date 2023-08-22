from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def Insert_Topic(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    return HttpResponse('Data is insertd successfully ')

def Insert_Webpage(requset):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    n=input('enter name:')
    u=input('enter url:')
    wo=Webpage.objects.get_or_create(Topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('Data is insertd successfully!!! ')

def Insert_AccessRecords(requset):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    n=input('enter name:')
    u=input('enter url:')
    wo=Webpage.objects.get_or_create(Topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('enter date:')
    a=input('enter author:')
    e=input('enter email:')
    ao=AccessRecords.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    return HttpResponse('Data is insertd successfully ')



