from django.conf.urls import patterns, include, url
from django_cas.views import login, logout  
from django.views.decorators.csrf import csrf_exempt

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('simplecmdb.views',
    # Examples:
    # url(r'^$', 'mytest.views.home', name='home'),
    # url(r'^mytest/', include('mytest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^collect/$', 'CollectHostInfo'),
    url(r'^$', 'summary'),
    url(r'^servers/$', 'servers'),
    url(r'^servers/(?P<host>[A-Za-z]+.+)/', 'jump_zabbix', name='zabbix'),
	url(r'^servers/(?P<ip>\d+\.\d+\.\d+\.\d+)/$', 'connect', name='connect'),
    url(r'^pd/(?P<pd_name>.+)/$', 'pd', name="pd"),
    url(r'^help/$', 'help'),
)

urlpatterns += patterns('django_cas.views',
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    )
