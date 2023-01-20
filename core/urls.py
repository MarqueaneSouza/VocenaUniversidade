from django.contrib import admin
from django.urls import path, include

from pagina.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagina.urls')), #quando o usuário digitar só o endereço localhost, ele vai carregar as urls da minha aplicação pagina1.
]
