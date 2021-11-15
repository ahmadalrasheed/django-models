from django.shortcuts import render
from django.views.generic import  ListView , DetailView
from .models import Snack

class Snacklistview(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailview(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
    context_object_name = "snack_object"


# Create your views here.



