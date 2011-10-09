from django.conf.urls.defaults import patterns, include, url
from ewidencja.views import main_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'grosik/$',main_page),
    # Examples:
    # url(r'^$', 'grosik.views.home', name='home'),
    # url(r'^grosik/', include('grosik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
