#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AlbumListView.as_view(), name='album_list'),
    url(r'^(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^create$', views.AlbumCreateView.as_view(), name='album_create'),
    url(r'^(?P<pk>\d+)/update$', views.AlbumUpdateView.as_view(), name='album_update'),
    url(r'^(?P<pk>\d+)/delete$', views.AlbumDeleteView.as_view(), name='album_delete'),
]

# TODO: change pk to slug in URLs
