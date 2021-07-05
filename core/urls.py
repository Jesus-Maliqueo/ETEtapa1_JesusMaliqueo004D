from django.urls import path
from .views import index,ingresarColabs,mostrar,modcolabs,delete_colabs,image_url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('ingresar',ingresarColabs,name='ingresar'),
    path('mostrar',mostrar,name="mostrar"),
    path('modificar/<id>',modcolabs,name="modificar"),
    path('eliminar/<id>',delete_colabs,name="eliminar"),
    path('image_url',image_url,name="image_url"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
