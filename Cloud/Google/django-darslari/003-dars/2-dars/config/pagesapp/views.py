from re import template
from django.shortcuts import render
from django.views.generic import TemplateView




# Create your views here.

class HomePageView(TemplateView): 
    template_name = 'home.html'

class AbboutPageView(TemplateView):
    template_name = 'about.html'

class YangiliklarPagesView(TemplateView):
    template_name = 'yangiliklar.html'

