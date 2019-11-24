"""
Definition of urls for acaizerograu.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'', include('home.urls')),
    url(r'^caixa/', include('caixa.urls')),
    url(r'^outros/', include('outros.urls')),
    url(r'^pedidos/', include('pedidos.urls')),
    url(r'^cliente/', include('cliente.urls')),
    url(r'^estoque/', include('estoque.urls')),
    # url(r'^login/$',
    #     django.contrib.auth.views.login,
    #     {
    #         'template_name': 'app/login.html',
    #         'authentication_form': app.forms.BootstrapAuthenticationForm,
    #         'extra_context':
    #         {
    #             'title': 'Log in',
    #             'year': datetime.now().year,
    #         }
    #     },
    #     name='login'),
    # url(r'^logout$',
    #     django.contrib.auth.views.logout,
    #     {
    #         'next_page': '/',
    #     },
    #     name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
