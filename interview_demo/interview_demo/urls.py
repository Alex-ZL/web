from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^board/(?P<board>\w+)', single_board),
	url(r'^topic/(?P<board>\w+)/(?P<pid>\w+)', post_detail),
	url(r'^boards/$', multiple_board),

    # Examples:
    # url(r'^$', 'interview_demo.views.home', name='home'),
    # url(r'^interview_demo/', include('interview_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
