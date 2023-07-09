from django.urls import path
from .views import TarjetaList

urlpatterns = [
    path('', TarjetaList.as_view(), name='tarjetas'),

]