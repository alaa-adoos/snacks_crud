from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Snack

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnackDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

class SnackCreateView(CreateView):
    template_name='snack_create.html'
    model=Snack
    fields=['purchaser','title','description','image_url']