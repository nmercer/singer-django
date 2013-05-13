from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('sing.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()