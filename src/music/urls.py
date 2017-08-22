#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from music.views import AlbumListView, AlbumCreateView, AlbumDetailView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name='album_list'),
    url(r'^create$', AlbumCreateView.as_view(), name='album_create'),
    url(r'^(?P<slug>[-\w]+)$', AlbumDetailView.as_view(), name='album_detail'),
    url(r'^(?P<slug>[-\w]+)/update$', AlbumUpdateView.as_view(), name='album_update'),
    url(r'^(?P<slug>[-\w]+)/delete$', AlbumDeleteView.as_view(), name='album_delete'),
]
