from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Elon(TemplateView):
    template_name = 'index.html'

class Musk(TemplateView):
    template_name = 'twitter.html'
