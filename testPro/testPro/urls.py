from django.conf.urls import patterns, include, url

from django.contrib import admin
from triWeb.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testPro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^performance_test/$', performance_test),
	(r'^$', index),
	(r'^dashboard/$',dashboard),
	(r'^assets/$', assets),
	(r'^status/$', getStatusData),
	(r'^squid_summary/$', squid_summary),
	(r'^graph/$', graph),
	(r'^get_squid_data/$', get_squid_data),
	(r'report_user_data/$', collect_user_data),
	(r'^stock/$', stock)
   
)


