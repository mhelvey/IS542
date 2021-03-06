from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^homepage/uploader_upload', 'homepage.views.upload'),
    url(r'^homepage/uploader', 'homepage.views.uploader'),
    url(r'^homepage/form', 'homepage.views.form'),
    url(r'^homepage/table/page/(?P<tpage>\d+)', 'homepage.views.table'),
    url(r'^homepage/table/', 'homepage.views.table'),
    url(r'^homepage/gallery', 'homepage.views.gallery'),
    url(r'^homepage/', 'homepage.views.base'),

    # url(r'^form', 'homepage.views.form'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'homepage.views.base', name='home'),
)


#     url(r'^table/page/(?P<page>\d+)/$', 'home.views.table'),
