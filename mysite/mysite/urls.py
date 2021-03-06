from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from myapp.api import EntryResource, UserResource
from view import *
from books import views
from contact import views as Cviews
from django.contrib import admin
from tastypie.api import Api
from dnsms.api import ArecordResource


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())
v1_api.register(ArecordResource())

urlpatterns = patterns('',
	(r'^now/$', current_datetime),
	#(r'^now/plus(\d{1,2})hours/$', hours_ahead),
	(r'^now/(plus|minus)(\d\d|[2-9])hours/$',hour_offset),
	(r'^now/(plus|minus)(1)hour/$',hour_offset),
	(r'^musicians/$',musicians),
	(r'^to-do-list1/$',todolist1),
    (r'^admin/', include(admin.site.urls)),
	(r'^show/', show_request_attribute),
	(r'^display/',display_meta),
	(r'^search-form/$', views.search_form),
	(r'^search/$', views.search),
	(r'^contact-form/$', Cviews.contact),
	#(r'^blog/', include(myapp.urls)),
	(r'^api/', include(v1_api.urls)),
)

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)
