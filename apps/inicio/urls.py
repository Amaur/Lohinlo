from django.conf.urls import patterns, include, url
from .views import Index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lohinlo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index',Index),

)
