from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codenamev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mediaplayer/', include('mediaplayer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
