from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pagina.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagina.urls')), #quando o usuário digitar só o endereço localhost, ele vai carregar as urls da minha aplicação pagina.
    path('como_funciona/', include('como_funciona.urls')),
    path('duvidas/', include('duvidas.urls')),
    path('inscricoes/', include('inscricoes.urls')),
    path('normas/', include('normas.urls')),

    path('login/', include('login.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
