
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.outros),
    url(r'^addadicional/$', views.addadicional),
    url(r'^addacai/$', views.addacai),
    url(r'^addcasadinho/$', views.addcasadinho),
    url(r'^addmix/$', views.addmix),
    url(r'^addcreme/$', views.addcreme),
    url(r'^addsorvete/$', views.addsorvete),
    url(r'^addmshake/$', views.addmshake),
    url(r'^addpetit/$', views.addpetit),
    url(r'^addfondue/$', views.addfondue),
    url(r'^addsuco/$', views.addsuco),
    url(r'^addproduto/$', views.addproduto),
    ]
