
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.caixa1),
    url(r'^extrato/$', views.extrato),
    url(r'^extrato_periodo/$', views.extrato_periodo),
    url(r'^retirada/$', views.retirada),
    url(r'^entrada/$', views.entrada),
    url(r'^fechar/$', views.fechar),
    url(r'^dados/$', views.dados),
    ]
