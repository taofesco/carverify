from django.shortcuts import render
from django.views.generic import *

class MainPage(TemplateView):
    template_name = "index.html"