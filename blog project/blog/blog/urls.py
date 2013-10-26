from django.conf.urls import url, patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'blog.views.index', name='index'),
	url(r'^page/(?P<page_index>\d+)/$', 'blog.views.index', name='index'),
	url(r'^about/$', 'blog.views.about', name='about'),
	url(r'^post/(?P<post_id>\d+)/$', 'blog.views.detail', name='detail'),
	url(r'^admin/', include(admin.site.urls))
)