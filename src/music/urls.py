#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from music.views import (AlbumCreate, AlbumDelete, AlbumDetail, AlbumDetailApi, AlbumList, AlbumListApi, AlbumUpdate,
                         TrackDetailApi, TrackListApi)

api_patterns = [
    url(r'^album/$', AlbumListApi.as_view()),
    url(r'^album/(?P<pk>\d+)/$', AlbumDetailApi.as_view()),
    url(r'^track/$', TrackListApi.as_view()),
    url(r'^track/(?P<pk>\d+)/$', TrackDetailApi.as_view()),
]

album_patterns = [
    url(r'^$', AlbumList.as_view(), name='list'),
    url(r'^create/$', AlbumCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', AlbumDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', AlbumUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', AlbumDelete.as_view(), name='delete'),
]

track_patterns = [
    # url(r'^api/(?P<pk>\d+)/$', TrackDetail.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', AlbumList.as_view(), name='album_list'),
    url(r'^album/', include(album_patterns, namespace='albums')),
    url(r'^track/', include(track_patterns, namespace='tracks')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
