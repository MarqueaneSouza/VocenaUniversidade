from django.urls import path
from . import views


urlpatterns = [
    path('leis', views.leis, name="leis"),
    path('decretos', views.decretos, name="decretos"),
    # path('', views.portarias, name="portarias"),
]