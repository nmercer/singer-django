from django.conf.urls import patterns, include, url

urlpatterns = patterns('sing.views',
    url(r'^$', 'view'),
    url(r'^callin$', 'callin'),
    url(r'^stepone$', 'stepone'),
    url(r'^record$', 'record'),
    url(r'^play$', 'play'),
)