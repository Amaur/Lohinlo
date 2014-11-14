from django.conf.urls import patterns, include, url
from .views import Index,Search,About , Cat, Archive

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lohinlo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index',Index),
    url(r'^search', Search),
    url(r'^about', About),
    url(r'^categ', Cat),
    url(r'^archives', Archive),

)
