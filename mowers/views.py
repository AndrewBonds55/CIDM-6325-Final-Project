# from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
#def homePageView(request):
 #   return HttpResponse("Welcome to Mowers!")

class HomePageView(TemplateView):
    template_name = "mowers/home.html"

class AboutPageView(TemplateView):
    template_name = "mowers/about.html"




