from django.urls import path
from . import views


urlpatterns = [
    path('', views.inscricoes, name="inscricoes"),
]