from django.conf.urls import patterns, url

from mediaplayer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<video_id>\d+)/$', views.play, name='play'),
    url(r'^(?P<video_id>\d+)/comment/$', views.comment, name='comment'),
)