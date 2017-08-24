#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from music.views import AlbumList, AlbumCreate, AlbumDetail, AlbumUpdate, AlbumDelete, AlbumListApi, AlbumDetailApi, \
    SongDetailApi

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

song_patterns = [
    url(r'^api/(?P<pk>\d+)/$', SongDetailApi.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', AlbumList.as_view(), name='album_list'),
    url(r'^albums/', include(album_patterns, namespace='albums')),
    url(r'^songs/', include(song_patterns, namespace='songs')),
]
