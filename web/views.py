from django.shortcuts import render
from django.http import  HttpResponse
from django.template import RequestContext,loader
# Create your views here.
def get_channel_list():
    pass
def home(request):
    context={'foo':'bar'}
    return render(request,'web/index.html',context)