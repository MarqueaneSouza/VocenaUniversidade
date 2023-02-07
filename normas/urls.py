from django.urls import path
from . import views


urlpatterns = [
    path('', views.leis, name="leis"),
    # path('', views.decretos, name="decretos"),
    # path('', views.portarias, name="portarias"),
]