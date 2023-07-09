from django.shortcuts import render
from django.views.generic import ListView
from .models import Tarjeta


class TarjetaList(ListView):
    model = Tarjeta
    template_name = 'appweb/index.html'
    
