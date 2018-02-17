#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from music.views import (AlbumCreate, AlbumDelete, AlbumDetail, AlbumList, AlbumUpdate, AlbumViewSet, ReactSample,
                         TrackViewSet)

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, base_name='album')
router.register(r'tracks', TrackViewSet, base_name='track')

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
    url(r'^albums/', include(album_patterns, namespace='albums')),
    url(r'^tracks/', include(track_patterns, namespace='tracks')),
    url(r'^react/', ReactSample.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
