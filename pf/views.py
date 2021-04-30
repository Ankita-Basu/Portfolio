from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

class HomePage(TemplateView):
    template_name='home.html'

class AboutPage(TemplateView):
    template_name='about.html'

class ContactPage(TemplateView):
    template_name='contact.html'