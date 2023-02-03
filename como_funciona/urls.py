from django.urls import path
from . import views


urlpatterns = [
    path('', views.como_funciona, name="como_funciona"),
]
