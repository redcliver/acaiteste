
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^novo_cliente/$', views.novo_cliente),
    url(r'^edita_cliente/$', views.edita_cliente),
    url(r'^salva_cliente/$', views.salva_cliente),
    url(r'^exclui_cliente/$', views.exclui_cliente),
    url(r'^dados_cliente/$', views.dados_cliente),
    ]
