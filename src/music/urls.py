#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from music.views import (AlbumCreate, AlbumDelete, AlbumDetail, AlbumDetailApi, AlbumList, AlbumListApi, AlbumUpdate,
                         TrackDetailApi)

album_api_patterns = [
    url(r'^$', AlbumListApi.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', AlbumDetailApi.as_view(), name='detail'),
]

album_patterns = [
    url(r'^$', AlbumList.as_view(), name='list'),
    url(r'^api/', include(album_api_patterns, namespace='api')),
    url(r'^create/$', AlbumCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', AlbumDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', AlbumUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', AlbumDelete.as_view(), name='delete'),
]

track_patterns = [
    url(r'^api/(?P<pk>\d+)/$', TrackDetailApi.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', AlbumList.as_view(), name='album_list'),
    url(r'^albums/', include(album_patterns, namespace='albums')),
    url(r'^tracks/', include(track_patterns, namespace='tracks')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
