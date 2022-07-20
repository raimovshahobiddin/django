from django.shortcuts import render
from django.http import HttpResponse, Httpresponse
# Create your views here.
def homePageView(request):
    return HttpResponse('hello world') 

