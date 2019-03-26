from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy


from django.views.generic import (TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'
